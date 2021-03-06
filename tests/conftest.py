import pytest
from src.base.faction import Faction
from src.base.module import Module
from src.base.position import Position
from src.base.entity import Entity
from src.base.frame import Frame


def get_test_faction() -> Faction:
    return Faction(
        tag="test_tag",
        accuracy_bonus=5,
        accuracy_multiplier=1.1,
        kinetic_damage_bonus=15,
        kinetic_damage_multiplier=1.10,
        energy_damage_bonus=10,
        energy_damage_multiplier=1.15,
        kinetic_weapon_range_bonus=100,
        kinetic_weapon_range_multiplier=1.10,
        energy_weapon_range_bonus=200,
        energy_weapon_range_multiplier=1.05,
    )


@pytest.fixture(scope="session")
def module():
    return Module(
        min_crew=10,
        max_crew=20,
        weight=200,
        fabricator=get_test_faction(),
        user=get_test_faction(),
        hp=1000,
        position=Position(x=10, y=10),
    )


@pytest.fixture(scope="session")
def entity1():
    return Entity(
        position=Position(x=0, y=0),
        frame=Frame(module_slots=6, max_hp=10000),
        faction=get_test_faction(),
        name="test entity",
    )


@pytest.fixture(scope="session")
def entity2():
    return Entity(
        position=Position(x=3, y=4),
        frame=Frame(module_slots=6, max_hp=10000),
        faction=get_test_faction(),
        name="test entity 2",
    )
