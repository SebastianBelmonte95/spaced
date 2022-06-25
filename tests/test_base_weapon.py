import pytest
from src.base.position import Position
from src.base.weapon import Weapon, WeaponType
from tests.conftest import get_test_faction


@pytest.fixture
def kinetic_weapon():
    return Weapon(
        min_crew=8,
        max_crew=14,
        weight=5000,
        weapon_type=WeaponType.KINETIC,
        base_damage=100,
        base_range=1000,
        base_accuracy=70,
        fabricator=get_test_faction(),
        user=get_test_faction(),
        hp=1000,
        position=Position(0, 0),
    )


@pytest.fixture
def energy_weapon():
    return Weapon(
        min_crew=8,
        max_crew=14,
        weight=5000,
        weapon_type=WeaponType.ENERGY,
        base_damage=100,
        base_range=1000,
        base_accuracy=60,
        fabricator=get_test_faction(),
        user=get_test_faction(),
        hp=1000,
        position=Position(0, 0),
    )


def test_kinetic_weapon_damage(kinetic_weapon):
    assert kinetic_weapon.damage == 125


def test_energy_weapon_damage(energy_weapon):
    assert energy_weapon.damage == 125


def test_kinetic_weapon_range(kinetic_weapon):
    assert kinetic_weapon.range == 1200


def test_energy_weapon_range(energy_weapon):
    assert energy_weapon.range == 1250


def test_kinetic_weapon_type(kinetic_weapon):
    assert kinetic_weapon.type == WeaponType.KINETIC


def test_energy_weapon_type(energy_weapon):
    assert energy_weapon.type == WeaponType.ENERGY


def test_accuracy(kinetic_weapon):
    assert kinetic_weapon.accuracy == 82
