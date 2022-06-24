from abc import ABC


class Module(ABC):
    def __init__(self, min_crew: int, max_crew: int, weight: int) -> None:
        self._min_crew = min_crew
        self._max_crew = max_crew
        self._weight = weight
    
    def min_crew(self):
        return self._min_crew

    def max_crew(self):
        return self._max_crew

    def weight(self):
        return self._weight
    