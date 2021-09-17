class IterablePoint(type):
    def __iter__(cls):
        return iter(cls.__name__)


class Point(metaclass=IterablePoint):
    def __init__(self, x, y, group):
        self.x = x
        self.y = y
        self.group = group

    def closest_point(self, points: list("Point")) -> "Point":
        return min(points, key=lambda p: Point.distance(self, p))

    def set_location(self, location):
        self.x = location[0]
        self.y = location[1]

    def __repr__(self) -> str:
        return f"(x={round(self.x, 2)}, y={round(self.y, 2)}, group={self.group})"

    @staticmethod
    def distance(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    @staticmethod
    def middle_of(points):
        x = sum([p.x for p in points]) / len(points)
        y = sum([p.y for p in points]) / len(points)
        return (x, y)


class RandomPoint(Point):
    def __init__(self, group):
        import random

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        super().__init__(x, y, group)


class RandomDonutDistributedPoint(Point):
    def __init__(self, group):
        import random

        while True:
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            r = (x ** 2 + y ** 2) ** 0.5
            if r > 0.7 or r < 0.3:
                break
        super().__init__(x, y, group)


class OddlyDistributedPoint(Point):
    def __init__(self, group):
        import random

        while True:
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            r1 = ((x - 0.5) ** 2 + (y - 0.3) ** 2) ** 0.5
            r2 = (x ** 2 + y ** 2) ** 0.5
            r3 = ((x + 0.1) ** 2 + (y + 0.7) ** 2) ** 0.5
            r4 = ((x + 0.7) ** 2 + (y + 0.7) ** 2) ** 0.5
            if min(r1, r2, r3, r4) < 0.35:
                break
        super().__init__(x, y, group)
