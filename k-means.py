NOT_YET_DETERMINED = -1
NUMBER_OF_ITERATION = 100


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


def cost_function(cluster_bases: list(Point), points: list(Point)) -> float:
    cost = 0.0
    for base in cluster_bases:
        for point in points:
            if base.group == point.group:
                cost += Point.distance(base, point) ** 2
    return cost


def k_means(num_of_clusters: int, points: list(Point)) -> list(Point):
    # get cluster bases
    cluster_bases = []
    for group in range(num_of_clusters):
        cluster_bases.append(RandomPoint(group))

    for trial in range(NUMBER_OF_ITERATION):
        for point in points:
            point.group = point.closest_point(cluster_bases).group
        for base in cluster_bases:
            my_points = list(filter(lambda p: p.group == base.group, points))
            if len(my_points) <= 0:
                raise Exception("number of points in a cluster is zero")
            base.set_location(Point.middle_of(my_points))
            point.group = point.closest_point(cluster_bases).group

        print(
            f"#{trial} cost : {round(cost_function(cluster_bases=cluster_bases, points=points), 2)}"
        )
    return points


def display(points: list(Point)):
    import matplotlib
    import matplotlib.pyplot as plt

    xs = [p.x for p in points]
    ys = [p.y for p in points]
    group = [p.group for p in points]

    plt.scatter(xs, ys, c=group, label=group)
    plt.show()


def test(num_of_clusters, num_of_points):
    points = list([RandomPoint(group=NOT_YET_DETERMINED) for _ in range(num_of_points)])
    display(k_means(num_of_clusters=num_of_clusters, points=points))


test(num_of_clusters=2, num_of_points=1000)
