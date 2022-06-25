from src.utils import distance_between


def test_distance_between(entity1, entity2):
    assert distance_between(entity1, entity2) == 5
