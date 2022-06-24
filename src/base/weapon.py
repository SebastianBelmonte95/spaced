from enum import Enum, auto
from src.base.module import Module
from src.base.faction import Faction


class WeaponType(Enum):
    ENERGY = auto
    KINETIC = auto


class Weapon(Module):
    def __init__(
        self,
        min_crew: int,
        max_crew: int,
        weight: int,
        weapon_type: WeaponType,
        base_damage: int,
        base_range: int,
        fabricator: Faction,
        user: Faction,
    ) -> None:
        super().__init__(min_crew, max_crew, weight)
        self._weapon_type = weapon_type
        self._fabricator = fabricator
        self._user = user
        self._base_damage = base_damage
        self._base_range = base_range

    @property
    def damage(self):
        if self._weapon_type == WeaponType.ENERGY:
            return int(
                (self._base_damage + self._fabricator.energy_damage_bonus)
                * self._fabricator.energy_damage_multiplier
            )
        elif self._weapon_type == WeaponType.KINETIC:
            return int(
                (self._base_damage + self._fabricator.kinetic_damage_bonus)
                * self._fabricator.kinetic_damage_multiplier
            )
