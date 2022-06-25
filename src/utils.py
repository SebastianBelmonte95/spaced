from math import sqrt


def distance_between(entity1, entity2) -> float:
    return sqrt(
        (entity2.get_position().x - entity1.get_position().x) ** 2
        + (entity2.get_position().y - entity1.get_position().y) ** 2
    )
