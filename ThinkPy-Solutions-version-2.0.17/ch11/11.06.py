#
# Exercise 6
# Run this version of fibonacci and the original with
# a range of parameters and compare their run times.
#
def fibonacci(n):
    if 0 == n:
        return 0
    elif 1 == n:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

known = {0:0, 1:1}
def fibonacci_memo(n):
    # If you announce known{} in here, it takes longer to run...
    if n in known:
        return known[n]

    res = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    known[n] = res
    return res



if "__main__" == __name__:
    # print fibonacci(35) #### for 1000 will get "RuntimeError: maximum recursion depth exceeded"
    print fibonacci_memo(35)