#
# Exercise 3
# To test the square root algorithm in this chapter,
# you could compare it with math.sqrt. Write a function
# named test_square_root that prints a table like this:
#
#   1.0 1.0           1.0           0.0
#   2.0 1.41421356237 1.41421356237 2.22044604925e-16
#   3.0 1.73205080757 1.73205080757 0.0
#   4.0 2.0           2.0           0.0
#   5.0 2.2360679775  2.2360679775  0.0
#   6.0 2.44948974278 2.44948974278 0.0
#   7.0 2.64575131106 2.64575131106 0.0
#   8.0 2.82842712475 2.82842712475 4.4408920985e-16
#   9.0 3.0           3.0           0.0
#
# The first column is a number, a; the second column is
# the square root of a computed with the function from
# Section 7.5; the third column is the square root computed
# by math.sqrt; the fourth column is the absolute value of
# the difference between the two estimates.
#
from math import sqrt

def square_root(a):
    x = a / 2
    epsilon = 0.000000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
        x = y

# print table
def test_square_root(a):
    result1 = square_root(a)
    result2 = sqrt(a)
    # print str(a) + " " + str(result1) + " " + str(result2) +" " + str(abs(result1-result2))
    # python format: http://www.python-course.eu/python3_formatted_output.php
    print "{0:s} {1:<13s} {2:<13s} {3:s}".format( str(a), str(result1), str(result2), str(abs(result1-result2)) )


def main():
    num = 1
    while num < 10:
        test_square_root(float(num))
        num += 1


if "__main__" == __name__:
    main()