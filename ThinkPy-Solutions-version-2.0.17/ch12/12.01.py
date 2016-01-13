#
# Exercise 1
# Many of the built-in functions use variable-length argument tuples.
# For example, max and min can take any number of arguments:
#   >>> max(1,2,3)
#   3
#
# But sum does not.
#   >>> sum(1,2,3)
#   TypeError: sum expected at most 2 arguments, got 3
#
# Write a function called sumall that takes any number of arguments
# and returns their sum.
#
def sumall(t):
    res = 0
    for element in t:
        if not type(element) == int:
            print "Some elements in the tuple are not int"
        res += element
    return res


if "__main__" == __name__:
    t = 10, 20, 50, 20
    print sumall(t)