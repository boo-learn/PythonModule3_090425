# Используя классы треугольника и окружности из предыдущих задач
# создайте список с произвольным набором фигур
# Найдите и выведите фигуры с наибольшей площадью
import random
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def area_triangle(self):
        # Находим длины сторон треугольника:
        a = self.point1.dist_to(self.point2)
        b = self.point2.dist_to(self.point3)
        c = self.point1.dist_to(self.point3)
        # Полу-периметр:
        half_p = (a + b + c) / 2
        # Для нахождения площади, используйте формулу Герона
        return (half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5


class Circle:
    def __init__(self, center_coords: tuple, radius):
        self.center_coords = Point(*center_coords)
        self.radius = radius

    def area_circle(self):
        return math.pi * self.radius ** 2


def create_random_list(num: int):
    list_ = []
    for _ in range(num):
        if random.choice([True, False]):
            p1 = Point(random.uniform(0, 10), random.uniform(0, 10))
            p2 = Point(random.uniform(0, 10), random.uniform(0, 10))
            p3 = Point(random.uniform(0, 10), random.uniform(0, 10))
            list_.append(Triangle(p1, p2, p3))
        else:
            center = (random.uniform(0, 10), random.uniform(0, 10))
            radius = random.uniform(0, 10)
            list_.append(Circle(center, radius))

    return list_

def max_area(figure_list: list):
    area_max_triangle = 0
    area_max_circle = 0
    for el in figure_list:
        if isinstance(el, Triangle) and el.area_triangle() > area_max_triangle:
            area_max_triangle = el.area_triangle()
        elif isinstance(el, Circle) and el.area_circle() > area_max_circle:
            area_max_circle = el.area_circle()
    return area_max_circle, area_max_triangle

figure = create_random_list(10)
area_max_triangle, area_max_circle = max_area(figure)

print(f"Наибольшая площадь треугольника: {area_max_triangle:.2f}")
print(f"Наибольшая площадь круга: {area_max_circle:.2f}")

#Vladimir Ghilas
