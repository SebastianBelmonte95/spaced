from dataclasses import dataclass


@dataclass
class Faction:
    tag: str
    cruise_speed_bonus: float = 0
    cruise_speed_multiplier: float = 1
    armor_bonus: float = 0
    armor_multiplier: float = 1
    hull_bonus: float = 0
    hull_multiplier: float = 1
    reload_speed_bonus: float = 0
    reload_speed_multiplier: float = 1
    kinetic_damage_bonus: float = 0
    kinetic_damage_multiplier: float = 1
    energy_damage_bonus: float = 0
    energy_damage_multiplier: float = 1
    building_speed_bonus: float = 0
    building_speed_multiplier: float = 1
    mining_speed_bonus: float = 0
    mining_speed_multiplier: float = 1
    research_speed_bonus: float = 0
    research_speed_multiplier: float = 1
    kinetic_weapon_range_bonus: float = 0
    kinetic_weapon_range_multiplier: float = 1
    energy_weapon_range_bonus: float = 0
    energy_weapon_range_multiplier: float = 1
