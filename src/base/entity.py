from abc import ABC
from typing import List
from src.base.position import Position
from src.base.module import Module
from src.base.faction import Faction


class Frame(ABC):
    def __init__(self, module_slots: int, max_hp: int) -> None:
        self._module_slots = module_slots
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def module_slots(self) -> int:
        return self._module_slots

    @property
    def hp(self) -> int:
        return self._hp

    @property
    def max_hp(self) -> int:
        return self._max_hp

    def destroy(self) -> None:
        print(f"{self} destroyed.")
        del self

    def set_hp(self, new_hp: int) -> None:
        self._hp = new_hp

    def set_max_hp(self, new_hp: int) -> None:
        self._max_hp = new_hp

    def reduce_hp(self, change: int) -> None:
        if change >= self._hp:
            self.destroy()
        self._hp -= change

    def repair(self, change: int) -> None:
        if self.hp + change > self.max_hp:
            self._hp = self.max_hp
        self._hp += change


class Entity(ABC):
    def __init__(
        self, position: Position, frame: Frame, faction: Faction, name: str
    ) -> None:
        super().__init__()
        self._position = position
        self._module_slots = list()
        self.frame = frame
        self.faction = faction
        self._name = name

    def move(self, new_position: Position) -> None:
        self._position = new_position

    def install_module(self, module: Module) -> None:
        if len(self._module_slots) > self.frame.module_slots:
            self._module_slots.append(module)
            print(f"{module} installed in {self._name}.")
            return
        print(f"{module} could not be installed in {self._name}. Module slots full")

    def get_modules(self) -> List[Module]:
        return self._module_slots
