from abc import ABC


class Armor(ABC):
    def __init__(self, density: float, kinetic_defense: float) -> None:
        self.density = density
        self.kinetic_defense = kinetic_defense
