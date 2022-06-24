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
    ) -> None:
        self._min_crew = min_crew
        self._max_crew = max_crew
        self._weight = weight
        self._fabricator = fabricator
        self._user = user

    @property
    def min_crew(self):
        return self._min_crew

    @property
    def max_crew(self):
        return self._max_crew

    @property
    def weight(self):
        return self._weight

    @property
    def fabricator(self):
        return self._fabricator.name

    @property
    def user(self):
        return self._user.name
