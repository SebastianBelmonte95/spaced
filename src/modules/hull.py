from abc import ABC


class Hull(ABC):
    def __init__(self, max_hp: int, size, hp: int) -> None:
        self.max_hp = max_hp
        self.hp = hp
        self.size = size
