from enum import Enum, auto
from src.base.module import Module
from src.base.faction import Faction
from src.utils import distance_between
from src.base.position import Position
from src.exceptions.position import NoPositionException


class WeaponType(Enum):
    ENERGY = auto()
    KINETIC = auto()


class Weapon(Module):
    def __init__(
        self,
        min_crew: int,
        max_crew: int,
        weight: int,
        hp: int,
        weapon_type: WeaponType,
        base_damage: int,
        base_range: int,
        base_accuracy: int,
        fabricator: Faction,
        user: Faction,
        name: str = "Weapon",
    ) -> None:
        super().__init__(min_crew, max_crew, weight, fabricator, user, hp, name)
        self._weapon_type = weapon_type
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

    def set_position(self, position: Position):
        # if hasattr(self,"position"):
        self._position = position

    def get_position(self):
        if hasattr(self, "_position"):
            return self._position
        else:
            raise NoPositionException(self)

    def is_in_range(self, target) -> bool:
        return distance_between(self, target) <= self.range
