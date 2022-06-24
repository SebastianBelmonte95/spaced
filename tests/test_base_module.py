import pytest
from src.base.module import Module


@pytest.fixture
def base_module():
    return Module(min_crew=10, max_crew=20, weight=200)


def test_min_crew(base_module):
    assert base_module.min_crew() == 10


def test_max_crew(base_module):
    assert base_module.max_crew() == 20


def test_weight(base_module):
    assert base_module.weight() == 200
