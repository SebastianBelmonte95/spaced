import pytest
from src.base.frame import Frame


@pytest.fixture(scope="function")
def frame():
    return Frame(module_slots=6, max_hp=10000)


def test_module_slots(frame):
    assert frame.module_slots == 6


def test_max_hp(frame):
    assert frame.max_hp == 10000


def test_hp(frame):
    assert frame.hp == 10000


@pytest.mark.parametrize("new_hp,expected", [(5000, 5000), (12000, 10000)])
def test_set_hp(frame, new_hp, expected):
    frame.set_hp(new_hp)
    assert frame.hp == expected


@pytest.mark.parametrize("new_hp,expected", [(5000, 5000), (12000, 12000)])
def test_set_max_hp_pass(frame, new_hp, expected):
    frame.set_max_hp(new_hp)
    assert frame.max_hp == expected


@pytest.mark.parametrize("new_hp", [(0), (-1)])
def test_set_max_hp_fail(frame, new_hp):
    with pytest.raises(ValueError):
        frame.set_max_hp(new_hp)


@pytest.mark.parametrize(
    "change,expected",
    [(5000, 5000), (2000, 8000), pytest.param(12000, 0, marks=pytest.mark.xfail)],
)
def test_reduce_hp(frame, change, expected):
    frame.reduce_hp(change)
    assert frame.hp == expected


@pytest.mark.parametrize(
    "change,expected",
    [(5000, 10000), (2000, 7000), (7000, 10000)],
)
def test_repair(frame, change, expected):
    frame.reduce_hp(5000)
    print(frame.hp)
    frame.repair(change)
    assert frame.hp == expected
