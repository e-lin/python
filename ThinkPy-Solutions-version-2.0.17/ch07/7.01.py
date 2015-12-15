#
# Exercise 1
# Rewrite the function print_n from Section 5.8 using iteration instead of recursion.
#

def print_n(s, n):
    while n != 0:
        print s
        n -= 1



def main():
    print_n("Peggy", 5)

if "__main__" == __name__:
    main()