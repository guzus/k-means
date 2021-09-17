from point import Point, RandomPoint, RandomDonutDistributedPoint, OddlyDistributedPoint

NUMBER_OF_ITERATION = 100


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
