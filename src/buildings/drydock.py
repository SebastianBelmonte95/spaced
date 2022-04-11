from dataclasses import field
from time import sleep


class Shipyard:
    def __init__(
        self,
        crew_capacity: int,
        crew: int,
        repair_bays: int,
        building_bays: int,
    ) -> None:
        self.crew_capacity = crew_capacity
        self.crew = crew
        self.repair_bays = repair_bays
        self.building_bays = building_bays

    def __post_init__(self):
        self.building_queue = []
        self.building_speed = 1
        self.repair_queue = []
        self.repair_speed = 1

    @property
    def efficiency(self):
        return round(self.crew / self.crew_capacity, 2)

    def add_ship_to_repair_queue(self, ship) -> None:
        self.repair_queue.append(ship)

    def repair(self) -> None:

        # REVIEW PYTHON QUEUE MODULE https://docs.python.org/3/library/queue.html
        for _ in range(self.repair_bays):
            ship = self.repair_queue.pop(0)
            while ship.hull < ship.max_hull:
                ship.hull += int(self.repair_speed * self.efficiency)
                sleep(100)
