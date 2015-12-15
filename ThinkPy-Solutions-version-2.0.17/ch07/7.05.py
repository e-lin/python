#
# Exercise 5
# The mathematician Srinivasa Ramanujan found an infinite series
# that can be used to generate a numerical approximation of 1/pi.
# ...skip formula...
#
# Write a function called estimate_pi that uses this formula to
# compute and return an estimate of pi. It should use a while loop
# to compute terms of the summation until the last term is smaller
# than 10^-15. You can check the result by comparing it to math.pi.
#
from math import factorial
from math import sqrt

def estimate_pi():
    epsilon = 1e-15 # which is python notation for 10^-15
    result = 0
    k = 0
    while True:
        num = factorial(4*k)*(1103+26390*k)
        den = pow(factorial(k), 4) * pow(396, 4*k)
        k_term = float(num) / float(den)

        if k_term < epsilon:
            break
        else:
            result += k_term
            k += 1
    pi = 2*sqrt(2)/9801 * result
    return 1 / pi


def main():
    print estimate_pi()

if "__main__" == __name__:
    main()
