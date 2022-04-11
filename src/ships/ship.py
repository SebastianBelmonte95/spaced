from abc import ABC
from typing import Any, List
from src.ships.engines import Engine
from src.misc.modules import Armor, Weapon, FTLDrive, DockingBay, Fuel
from src.characters.base import Officer


class Ship(ABC):
    def __init__(
        self,
        captain: Officer,
        ideal_officer_count: int,
        officers: int,
        ideal_crew_count: int,
        crew_capacity: int,
        crew: int,
        engines: List[Engine],
        fuel_capacity: float,
        fuel: float,
        fuel_type: Fuel,
        cargo_volume_capacity: float,
        cargo: List[Any],
        armor: Armor,
        weapons: dict,  # {"large": List[Weapon], "medium": List[Weapon], "small": List[Weapon], "epic": List[Weapon]}
        ftl_drive: FTLDrive,
        docking_bays: List[DockingBay],
    ):
        self.captain = captain
        self.ideal_officer_count = ideal_officer_count
        self.officers = officers
        self.ideal_crew_count = ideal_crew_count
        self.crew_capacity = crew_capacity
        self.crew = crew
        self.engines = engines
        self.fuel_capacity = fuel_capacity
        self.fuel = fuel
        self.fuel_type = fuel_type
        self.cargo_volume_capacity = cargo_volume_capacity
        self.cargo = cargo
        self.armor = armor
        self.weapons = weapons
        self.ftl_drive = ftl_drive
        self.docking_bays = docking_bays

    @property
    def displacement(self):
        return

    @property
    def weapons_weight(self) -> float:
        weight = 0
        for weapon_type in self.weapons:
            weight += sum(weapon.weight for weapon in weapon_type)
        return weight

    @property
    def weight(self) -> float:
        engine_weight = sum([engine.weight for engine in self.engines])
        fuel_weight = round(self.fuel * self.fuel_type.density, 2)
        armor_weight = self.armor.density * self.displacement / 100
        cargo_weight = round(
            sum([cargo_object.weight for cargo_object in self.cargo]), 2
        )
        return engine_weight + fuel_weight + armor_weight + cargo_weight

    @property
    def engine_power(self) -> float:
        return sum([engine.power for engine in self.engines])

    @property
    def weight_penalty(self) -> float:
        if self.weight < (0.33 * self.engine_power):
            return 0.0
        if self.weight < (0.66 * self.engine_power):
            return 0.5
        return 0.85

    @property
    def crew_efficiency(self) -> float:
        if self.crew < self.ideal_crew_count:
            return round(self.crew / self.ideal_crew_count, 2)
        return 1.0

    @property
    def officer_efficiency(self) -> float:
        if self.officers < self.ideal_officer_count:
            return round(self.crew / self.ideal_officer_count, 2)
        return 1.0

    @property
    def speed_multiplier(self):
        multiplier = (
            self.crew_efficiency
            + self.officer_efficiency
            + self.fuel_type.efficiency
            + self.captain.speed_bonus
            - self.weight_penalty
        )
        return multiplier

    @property
    def speed(self) -> float:
        if self.speed_multiplier < 0:
            return 0
        return self.engine_power * self.speed_multiplier

    @property
    def ftl_speed(self) -> float:
        if self.speed_multiplier < 0:
            return 0
        return self.ftl_drive.speed * self.speed_multiplier

    @property
    def fuel_consumption(self) -> float:
        return (
            sum([engine.consumption for engine in self.engines])
            * self.fuel_type.efficiency
        )

    @property
    def max_autonomy(self) -> float:
        return (self.fuel_capacity / self.fuel_consumption) * self.speed

    @property
    def autonomy(self) -> float:
        return (self.fuel / self.fuel_consumption) * self.speed
