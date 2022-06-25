from abc import ABC
from typing import List, Tuple
from src.base.position import Position
from src.base.module import Module
from src.base.faction import Faction
from src.base.frame import Frame


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

    @property
    def position(self) -> Tuple[float, float]:
        return self._position.x, self._position.y

    @property
    def free_module_slots(self) -> int:
        return self.frame.module_slots - len(self._module_slots)

    def has_free_slots(self) -> bool:
        return len(self._module_slots) > self.frame.module_slots

    def install_module(self, module: Module) -> None:
        if self.has_free_slots():
            self._module_slots.append(module)
            print(f"{module} installed in {self._name}.")
            return
        print(f"{module} could not be installed in {self._name}. Module slots full")

    def get_modules(self) -> List[Module]:
        return self._module_slots
