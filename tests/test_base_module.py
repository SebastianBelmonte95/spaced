import pytest
from src.base.module import Module
from src.base.position import Position
from tests.conftest import get_test_faction


@pytest.fixture
def base_module():
    return Module(
        min_crew=10,
        max_crew=20,
        weight=200,
        fabricator=get_test_faction(),
        user=get_test_faction(),
        hp=1000,
        position=Position(0, 0),
    )


def test_min_crew(base_module):
    assert base_module.min_crew == 10


def test_max_crew(base_module):
    assert base_module.max_crew == 20


def test_weight(base_module):
    assert base_module.weight == 200


def test_fabricator(base_module):
    assert base_module.fabricator == "Faction"


def test_user(base_module):
    assert base_module.user == "Faction"


def test_hp(base_module):
    assert base_module.hp == 1000


def test_position(base_module):
    x, y = base_module.position()
    assert x == 0
    assert y == 0


def test_set_position(base_module):
    base_module.set_position(Position(-5, 5))
    x, y = base_module.position()
    assert x == -5
    assert y == 5


def test_get_position(base_module):
    pos = base_module.get_position()
    expected = Position(0, 0)
    assert pos.x == expected.x
    assert pos.y == expected.y
