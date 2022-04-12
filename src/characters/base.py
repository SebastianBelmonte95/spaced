from abc import ABC


class Officer(ABC):
    def __init__(self, speed_bonus: float) -> None:
        self.speed_bonus = speed_bonus
