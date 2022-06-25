from abc import ABC


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
