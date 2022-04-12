from dataclasses import dataclass
from typing import List


@dataclass
class Engine:
    weight: float
    speed: float
    consumption: float
    power: float
