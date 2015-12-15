#
# Exercise 2
# Encapsulate this loop in a function called square_root
# that takes a as a parameter, chooses a reasonable value
# of x, and returns an estimate of the square root of a.
#

def square_root(a):
    x = a / 2
    epsilon = 0.000000000001
    while True:
        y = (x + a/x) / 2
        print y
        if abs(y-x) < epsilon:
            break
        x = y


def main():
    num = raw_input('Square root of what?\n')
    square_root(float(num))

if "__main__" == __name__:
    main()

