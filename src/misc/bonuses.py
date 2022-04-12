from dataclasses import dataclass


@dataclass
class FactionBonus:
    speed_multiplier: float = 0
    speed_increase: int = 0
    armor_resistance: int = 0
    hull_hp: int = 0
    hull_resistance: float = 0
    piercing_bonus: int = 0
    kinetic_damage_multiplier: float = 0
    energy_damage_multiplier: float = 0
    building_speed: float = 0
    engine_power_multiplier: float = 0
