from abc import ABC


class FTLDrive(ABC):
    def __init__(self, speed: float) -> None:
        self.speed = speed


class DockingBay(ABC):
    def __init__(self) -> None:
        super().__init__()


class Fuel(ABC):
    def __init__(self, efficiency: float, density: float) -> None:
        self.efficiency = efficiency
        self.density = density
