from abc import ABC
from dataclasses import dataclass
from src.misc.bonuses import FactionBonus


@dataclass
class Faction(ABC):
    tag: str
    bonus: FactionBonus
