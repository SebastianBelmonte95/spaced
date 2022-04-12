from abc import ABC, abstractmethod
from src.factions.base import Faction
from src.factions.humans import Humans
from src.modules.armor import Armor
from src.modules.hull import Hull
from src.modules.weapons import Weapon
from src.modules.misc import FTLDrive, Fuel
from src.ships.engines import Engine
from src.ships.ship import Ship
from src.misc.constants import SPEED_OF_LIGHT


class ShipFactory(ABC):
    def __init__(self, faction: Faction) -> None:
        self.faction = faction

    @abstractmethod
    def build_small_ship(self) -> Ship:
        pass

    # @abstractmethod
    # def build_medium_ship(self) -> Ship:
    #     pass

    # @abstractmethod
    # def build_large_ship(self) -> Ship:
    #     pass

    # @abstractmethod
    # def build_titan(self) -> Ship:
    #     pass


class HumanShipFactory(ShipFactory):
    def __init__(self, faction=Humans) -> None:
        self.faction = faction

    def build_small_ship(self) -> Ship:
        ship_id = f"{self.faction.tag}-{1}"
        hull = Hull(max_hp=2500, hp=2500, size="small")
        engines = [Engine(weight=3000, speed=1500, consumption=10, power=50000)]
        ftl_drive = FTLDrive(speed=1.2 * SPEED_OF_LIGHT)
        fuel = Fuel(efficiency=1.0, density=1.85)
        armor = Armor(density=7.85, kinetic_defense=100.0)
        weapons = {"small": [Weapon(), Weapon()]}
        small_ship = Ship(
            id=ship_id,
            ideal_crew_count=60,
            ideal_officer_count=5,
            officers=5,
            crew=60,
            crew_capacity=80,
            hull=hull,
            engines=engines,
            fuel_capacity=1500,
            fuel_type=fuel,
            fuel=1500,
            ftl_drive=ftl_drive,
            cargo_volume_capacity=1000,
            cargo=[],
            armor=armor,
            weapons=weapons,
            docking_bays=None,
            captain=None,
        )
        return small_ship

    # def build_medium_ship(self) -> Ship:
    #     return small_ship

    # def build_large_ship(self) -> Ship:
    #     return small_ship

    # def build_titan(self) -> Ship:
    #     return small_ship
