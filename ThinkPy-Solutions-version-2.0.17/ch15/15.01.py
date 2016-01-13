#
# Exercise 1
# Write a function called distance_between_points that takes
# two Points as arguments and returns the distance between them.
#
import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_between_points(p, q):
    x_dis = float(p.x) - float(q.x)
    y_dis = float(p.y) - float(q.y)

    return math.sqrt(x_dis**2 + y_dis**2)


if "__main__" == __name__:
    a = Point(0, 0)
    b = Point(3, 4)
    print distance_between_points(a, b)