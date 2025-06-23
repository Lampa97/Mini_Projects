import pytest

from projects.project_1_sequences import Polygon, PolygonSequence


@pytest.fixture
def polygon_1():
    """Fixture for a polygon with 3 edges and radius 2."""
    return Polygon(3, 2)


@pytest.fixture
def polygon_2():
    """Fixture for a polygon with 4 edges and radius 5."""
    return Polygon(4, 5)


@pytest.fixture
def polygon_3():
    """Fixture for a polygon with 4 edges and radius 5."""
    return Polygon(4, 5)


@pytest.fixture
def polygon_sequence_1():
    """Fixture for a PolygonSequence with max edges 10 and radius 5."""
    return PolygonSequence(10, 5)
