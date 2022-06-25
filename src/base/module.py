from abc import ABC
from src.base.faction import Faction


class Module(ABC):
    def __init__(
        self,
        min_crew: int,
        max_crew: int,
        weight: int,
        fabricator: Faction,
        user: Faction,
        hp: int,
        module_name: str = "Module",
    ) -> None:
        self._min_crew = min_crew
        self._max_crew = max_crew
        self._weight = weight
        self._fabricator = fabricator
        self._user = user
        self._hp = hp
        self._name = module_name

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

    def destroy(self) -> None:
        print(f"{type(self)} destroyed.")
        del self
