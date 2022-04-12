from src.misc.bonuses import FactionBonus
from src.factions.base import Faction


class Humans(Faction):
    tag = "UNS"
    bonus = FactionBonus(kinetic_damage_multiplier=0.15, building_speed=0.05)
