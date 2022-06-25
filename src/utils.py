from math import sqrt


def distance_between(entity1, entity2) -> float:
    return sqrt(
        (entity2.position.x - entity1.position.x) ** 2
        - (entity2.position.y - entity1.position.y) ** 2
    )
