from queue import Queue
from src.ships.ship import Ship
from src.utils.utils import logger
from time import sleep
from src.ships.factories import ShipFactory


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
        self.building_queue = Queue(maxsize=10)
        self.base_building_speed = 1
        self.active_building_queue = Queue(maxsize=self.building_bays)
        self.repair_queue = Queue(maxsize=100)
        self.base_repair_speed = 1
        self.active_repair_queue = Queue(maxsize=self.repair_bays)

    @property
    def efficiency(self):
        return round(self.crew / self.crew_capacity, 2)

    @property
    def repair_speed(self) -> float:
        return round(self.efficiency * self.base_repair_speed, 1)

    @property
    def building_speed(self) -> float:
        return round(self.efficiency * self.base_building_speed, 1)

    def add_ship_to_repair_queue(self, ship) -> None:
        self.repair_queue.put(ship, block=True)

    def repair(self) -> None:
        # REVIEW PYTHON QUEUE MODULE https://docs.python.org/3/library/queue.html
        for _ in range(self.repair_bays):
            ship = self.repair_queue.get()
            logger("Repairing " + ship)
            while ship.hull < ship.max_hull:
                ship.hull += int(self.repair_speed * self.efficiency)
                sleep(0.1)
            logger(f"Ship {ship.id} repaired!")

    def build_ship(self, ship_factory: ShipFactory) -> Ship:
        logger("Building ship...")
        sleep(2)
        ship = ship_factory.build_small_ship()
        logger(f"{ship.hull.size.capitalize()} ship built!")
        return ship
