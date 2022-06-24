from enum import Enum, auto
from src.base.module import Module
from src.base.faction import Faction


class WeaponType(Enum):
    ENERGY = auto()
    KINETIC = auto()


class Weapon(Module):
    def __init__(
        self,
        min_crew: int,
        max_crew: int,
        weight: int,
        weapon_type: WeaponType,
        base_damage: int,
        base_range: int,
        base_accuracy: int,
        fabricator: Faction,
        user: Faction,
    ) -> None:
        super().__init__(min_crew, max_crew, weight)
        self._weapon_type = weapon_type
        self._fabricator = fabricator
        self._user = user
        self._base_damage = base_damage
        self._base_range = base_range
        self._base_accuracy = base_accuracy

    @property
    def damage(self) -> int:
        if self._weapon_type == WeaponType.ENERGY:
            return round(
                (self._base_damage * self._fabricator.energy_damage_multiplier)
                + self._fabricator.energy_damage_bonus
            )
        elif self._weapon_type == WeaponType.KINETIC:
            return round(
                (self._base_damage * self._fabricator.kinetic_damage_multiplier)
                + self._fabricator.kinetic_damage_bonus
            )
        return self._base_damage

    @property
    def range(self) -> int:
        if self._weapon_type == WeaponType.ENERGY:
            return round(
                (self._base_range * self._fabricator.energy_weapon_range_multiplier)
                + self._fabricator.energy_weapon_range_bonus
            )
        elif self._weapon_type == WeaponType.KINETIC:
            return round(
                (self._base_range * self._fabricator.kinetic_weapon_range_multiplier)
                + self._fabricator.kinetic_weapon_range_bonus
            )
        return self._base_range

    @property
    def accuracy(self) -> int:
        return round(
            (self._base_accuracy * self._fabricator.accuracy_multiplier)
            + self._fabricator.accuracy_bonus
        )

    @property
    def type(self):
        return self._weapon_type
