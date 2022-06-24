import pytest
from src.base.module import Module
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
