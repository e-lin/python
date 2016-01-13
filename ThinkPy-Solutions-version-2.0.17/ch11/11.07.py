#
# Exercise 7
# Memoize the Ackermann function from Exercise 5 and see if
# memoization makes it possible to evaluate the function with
# bigger arguments. Hint: no.
# Solution: http://thinkpython.com/code/ackermann_memo.py.
#
def ackermann(m, n):
    """n, m: non-negative integers"""
    if 0 == m:
        return n+1
    if 0 == n:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m,n-1))


### To think m,n as a matrix, acker(m,n) equals to acker(m-1, index). The index is acker(m,n-1).
# n\m  0 1 2 3 4 5
#     ------------
#  0 | 1 2 3 5 $
#  1 | 2 3 5 ? *
#  2 | 3 4 7
#  3 | 4 5
#  4 | 5 6
#  5 | 6 7
#
# So we create a known dictionary where m is key, n is a list of values
m0_nlist = []
m1_nlist = []
for n in range(50):
    m0_nlist.append(n+1)
    m1_nlist.append(n+2)
known = { 0:m0_nlist, 1:m1_nlist }

def ackermann_memo(m, n):
    if m in known:
        if n < len(known[m]): # notice that here n means index
            return known[m][n]
        else: # case of "?" in above figure
            res = ackermann(m-1, ackermann(m,n-1))
            known[m].append(res)
            return res
    else:
        known[m] = [] # create an empty n-list for column m

        if n == 0: # case of "$" in above figure
            res = ackermann(m-1, 1)
            known[m].append(res)
            return res
        else: # case of "*" in above figure
            res = ackermann(m-1, ackermann(m,n-1))
            known[m].append(res)
            return res


cache = {}
def ackerman_solution(m, n):
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)

    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m,n-1))
        return cache[m, n]



if "__main__" == __name__:
    print ackermann(3, 6)
    print ackermann_memo(3, 6)
    print ackerman_solution(3, 6)

