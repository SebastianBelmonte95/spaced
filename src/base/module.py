from abc import ABC
from typing import Tuple
from src.base.faction import Faction
from src.base.position import Position
from src.exceptions.position import NoPositionException


class Module(ABC):
    def __init__(
        self,
        min_crew: int,
        max_crew: int,
        weight: int,
        fabricator: Faction,
        user: Faction,
        hp: int,
        position: Position,
        module_name: str = "Module",
    ) -> None:
        self._min_crew = min_crew
        self._max_crew = max_crew
        self._weight = weight
        self._fabricator = fabricator
        self._user = user
        self._hp = hp
        self._name = module_name
        self._position = position

    def __str__(self) -> str:
        return self._name

    @property
    def min_crew(self) -> int:
        return self._min_crew

    @property
    def max_crew(self) -> int:
        return self._max_crew

    @property
    def weight(self) -> int:
        return self._weight

    @property
    def fabricator(self) -> str:
        return self._fabricator.name

    @property
    def user(self) -> str:
        return self._user.name

    @property
    def hp(self) -> int:
        return self._hp

    def set_position(self, new_position: Position) -> None:
        self._position = new_position

    def get_position(self) -> Position:
        return self._position

    def position(self) -> Tuple[float, float]:
        return self._position.x, self._position.y
