#
# Exercise 4
# The built-in function eval takes a string and evaluates it using the Python interpreter.
# For example:
#
#   >>> eval('1 + 2 * 3')
#   7
#   >>> import math
#   >>> eval('math.sqrt(5)')
#   2.2360679774997898
#   >>> eval('type(math.pi)')
#   <type 'float'>
#
# Write a function called eval_loop that iteratively prompts the user, takes the resulting
# input and evaluates it using eval, and prints the result. It should continue until the
# user enters 'done', and then return the value of the last expression it evaluated.
#
import math

def eval_loop():
    while True:
        s = raw_input('what do you want to eval?\n')
        if 'done' == s:
            break
        else:
            print eval(s)


def main():
    eval_loop()

if "__main__" == __name__:
    main()