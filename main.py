from src.buildings.shipyard import Shipyard
from src.ships.factories import HumanShipFactory


def main():
    shipyard = Shipyard(crew_capacity=1500, crew=1500, repair_bays=2, building_bays=2)

    small_ship = shipyard.build_ship(ship_factory=HumanShipFactory())
    print(small_ship)


if __name__ == "__main__":
    main()
