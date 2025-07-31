import pytest

from projects.project_1_sequences import Polygon, PolygonSequence


def test_polygon_initialization(polygon_1):
    """Test the initialization of a Polygon."""
    assert polygon_1._edges == 3
    assert polygon_1._radius == 2
    assert polygon_1.interior_angle == 60.0
    assert polygon_1.edge_length == pytest.approx(3.46, abs=0.01)
    assert polygon_1.apothem == pytest.approx(1.0, abs=0.01)
    assert polygon_1.area == pytest.approx(5.19, abs=0.01)
    assert polygon_1.perimeter == pytest.approx(10.39, abs=0.01)


def test_polygon_repr(polygon_1):
    """Test the string representation of a Polygon."""
    assert repr(polygon_1) == "Polygon(edges=3, radius=2)"


def test_polygon_str(polygon_1):
    """Test the string output of a Polygon."""
    assert str(polygon_1) == "Polygon with 3 edges and radius 2"


def test_polygon_equality(polygon_1, polygon_2, polygon_3):
    """Test the equality operator for Polygons."""
    assert polygon_1 == Polygon(3, 2)
    assert polygon_1 != polygon_2
    assert polygon_2 == polygon_3
    assert polygon_2 != Polygon(5, 5)


def test_polygon_comparison(polygon_1, polygon_2):
    """Test the greater than operator for Polygons."""
    assert polygon_2 > polygon_1
    assert not (polygon_1 > polygon_2)
    assert not (polygon_1 > Polygon(3, 2))  # Same edges, should not be greater
    assert polygon_2 > Polygon(3, 2)  # More edges, should be greater


def test_polygon_init_errors():
    """Test initialization errors for Polygon."""
    with pytest.raises(TypeError):
        Polygon("three", 2)  # edges should be an int
    with pytest.raises(TypeError):
        Polygon(3, "two")  # radius should be an int
    with pytest.raises(ValueError):
        Polygon(2, 2)  # A polygon with fewer than 3 edges is not valid


def test_polygon_with_other_types():
    """Test comparison with non-Polygon types."""
    polygon = Polygon(3, 2)
    with pytest.raises(TypeError):
        assert polygon > 2
    with pytest.raises(TypeError):
        assert polygon > "string"
    with pytest.raises(TypeError):
        assert polygon == [1, 2, 3]


def test_polygon_sequence_initialization(polygon_sequence_1):
    """Test the initialization of a PolygonSequence."""
    assert polygon_sequence_1.max_edges == 10
    assert polygon_sequence_1.radius == 5
    assert len(polygon_sequence_1) == 8  # Polygons with edges from 3 to 10
    assert polygon_sequence_1[0]._edges == 3
    assert polygon_sequence_1[7]._edges == 10
    assert (
        polygon_sequence_1.max_efficiency_polygon == polygon_sequence_1[7]
    )  # Polygon with 10 edges should have the highest area/perimeter ratio


def test_polygon_sequence_slicing(polygon_sequence_1):
    """Test slicing of PolygonSequence."""
    assert polygon_sequence_1[0]._edges == 3
    assert polygon_sequence_1[1]._edges == 4
    assert polygon_sequence_1[-1]._edges == 10
    assert (
        polygon_sequence_1[:3][2]._edges == 5
    )  # Slicing should return the correct polygons


def test_polygon_sequence_init_error():
    """Test initialization errors for PolygonSequence."""
    with pytest.raises(TypeError):
        PolygonSequence("ten", 5)  # max_edges should be an int
    with pytest.raises(TypeError):
        PolygonSequence(10, "five")  # radius should be an int
    with pytest.raises(ValueError):
        PolygonSequence(2, 5)  # max_edges must be at least 3


def test_polygon_sequence_repr(polygon_sequence_1):
    """Test the string representation of a PolygonSequence."""
    assert repr(polygon_sequence_1) == "PolygonSequence(max_edges=10, radius=5)"


def test_polygon_sequence_str(polygon_sequence_1):
    """Test the string output of a PolygonSequence."""
    assert (
        str(polygon_sequence_1)
        == "PolygonSequence with polygons up to 10 edges and radius 5"
    )
