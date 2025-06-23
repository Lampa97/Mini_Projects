from math import pi, sin, cos

class Polygon:
    def __init__(self, edges: int, radius: int):
        if not isinstance(edges, int):
            raise TypeError("edges must be an int")
        if not isinstance(radius, int):
            raise TypeError("radius must be an int")
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

        def __eq__(self, other):
            if not isinstance(other, Polygon):
                return NotImplemented
            return (self.edges == other.edges and
                    self.radius == other.radius)

        def __gt__(self, other):
            if not isinstance(other, Polygon):
                return NotImplemented
            return self.edges > other.edges


