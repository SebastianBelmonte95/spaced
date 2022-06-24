from src.base.faction import Faction

def get_test_faction() -> Faction:
    return Faction(
        tag="test_tag",
        accuracy_bonus=5,
        accuracy_multiplier=1.1,
        kinetic_damage_bonus=15,
        kinetic_damage_multiplier=1.10,
        energy_damage_bonus=10,
        energy_damage_multiplier=1.15,
        kinetic_weapon_range_bonus=100,
        kinetic_weapon_range_multiplier=1.10,
        energy_weapon_range_bonus=200,
        energy_weapon_range_multiplier=1.05,
    )