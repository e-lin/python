#
# Import other files
# Reference: http://blog.eddie.com.tw/2011/10/13/python-module/
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