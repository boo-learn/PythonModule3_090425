from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        # TODO-0: скопируйте реализацию из предыдущей задачи
        ...


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

random_point = Point(-12, 0)
summa = 0
for point in points:
    dist = point.dist_to(random_point)
    summa += dist


print(f"Длина ломаной линии равна {round(summa, 2)}")
