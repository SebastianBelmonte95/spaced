import pytest
from src.base.entity import Entity
from src.base.frame import Frame
from src.base.position import Position
from tests.conftest import get_test_faction
from src.exceptions.entity import NoSlotsAvailableException


@pytest.fixture
def entity():
    return Entity(
        position=Position(x=0, y=0),
        frame=Frame(module_slots=6, max_hp=10000),
        faction=get_test_faction(),
        name="test entity",
    )


@pytest.fixture
def entity_1_slot():
    return Entity(
        position=Position(x=0, y=0),
        frame=Frame(module_slots=1, max_hp=10000),
        faction=get_test_faction(),
        name="test entity",
    )


@pytest.mark.parametrize(
    "new_position, expected_x, expected_y",
    [
        (Position(x=100, y=100), 100, 100),
        (Position(x=-100, y=100), -100, 100),
        (Position(x=100, y=-100), 100, -100),
        (Position(x=-100, y=-100), -100, -100),
    ],
)
def test_move(entity, new_position, expected_x, expected_y):
    entity.move(new_position)
    assert entity.position == (expected_x, expected_y)


def test_free_module_slots_init(entity):
    assert entity.free_module_slots == 6


def test_install_module_pass(entity, module):
    entity.install_module(module)
    assert entity.free_module_slots == 5
    assert entity.get_modules() == [module]


def test_install_module_fail(entity_1_slot, module):
    entity_1_slot.install_module(module)
    with pytest.raises(NoSlotsAvailableException):
        entity_1_slot.install_module(module)
    assert entity_1_slot.free_module_slots == 0
