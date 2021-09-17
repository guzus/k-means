from k_means import cost_function, k_means, display
from point import Point, RandomPoint, RandomDonutDistributedPoint, OddlyDistributedPoint

NOT_YET_DETERMINED = -1


def test(num_of_clusters, num_of_points):
    points = list([RandomPoint(group=NOT_YET_DETERMINED) for _ in range(num_of_points)])
    display(k_means(num_of_clusters=num_of_clusters, points=points))


def test_donut_distribution(num_of_clusters, num_of_points):
    points = list(
        [
            RandomDonutDistributedPoint(group=NOT_YET_DETERMINED)
            for _ in range(num_of_points)
        ]
    )
    display(k_means(num_of_clusters=num_of_clusters, points=points))


def test_odd_distribution(num_of_clusters, num_of_points):
    points = list(
        [OddlyDistributedPoint(group=NOT_YET_DETERMINED) for _ in range(num_of_points)]
    )
    display(k_means(num_of_clusters=num_of_clusters, points=points))


if __name__ == "__main__":
    # test(num_of_clusters=5, num_of_points=1000)
    # test_donut_distribution(num_of_clusters=3, num_of_points=1000)
    test_odd_distribution(num_of_clusters=5, num_of_points=1000)
