from math import cos, pi, sin


class Polygon:
    """A class representing a regular polygon with a specified number of edges and radius."""

    def __init__(self, edges: int, radius: int):
        if not isinstance(edges, int):
            raise TypeError("edges must be an int")
        if not isinstance(radius, int):
            raise TypeError("radius must be an int")
        if edges < 3:
            raise ValueError("A polygon must have at least 3 edges")
        self.edges = edges
        self.vertices = edges
        self.radius = radius
        self.interior_angle = (edges - 2) * 180 / edges
        self.edge_length = 2 * radius * sin(pi / edges)
        self.apothem = radius * cos(pi / edges)
        self.area = (self.edge_length * self.apothem * edges) / 2
        self.perimeter = self.edge_length * edges

    def __repr__(self):
        return f"Polygon(edges={self.edges}, radius={self.radius})"

    def __str__(self):
        return f"Polygon with {self.edges} edges and radius {self.radius}"

    def __eq__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError(
                "Equality not supported between instances of 'Polygon' and other types"
            )
        return self.edges == other.edges and self.radius == other.radius

    def __gt__(self, other):
        if not isinstance(other, Polygon):
            raise TypeError(
                "Comparison not supported between instances of 'Polygon' and other types"
            )
        return self.edges > other.edges


class PolygonSequence:
    """A class representing a sequence of polygons with edges ranging from 3 to a specified maximum."""

    def __init__(self, max_edges: int, radius: int):
        if not isinstance(max_edges, int) or not isinstance(radius, int):
            raise TypeError("max_edges and radius must be integers")
        if max_edges < 3:
            raise ValueError("max_edges must be at least 3")
        self.max_edges = max_edges
        self.radius = radius
        self.polygons = [Polygon(edges, radius) for edges in range(3, max_edges + 1)]
        self.max_efficiency_polygon = max(
            self.polygons, key=lambda p: p.area / p.perimeter
        )

    def __repr__(self):
        return f"PolygonSequence(max_edges={self.max_edges}, radius={self.radius})"

    def __str__(self):
        return f"PolygonSequence with polygons up to {self.max_edges} edges and radius {self.radius}"

    def __len__(self):
        return len(self.polygons)

    def __getitem__(self, item):
        return self.polygons[item]
