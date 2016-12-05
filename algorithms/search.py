# sequencial search : O(n)
def sequencial_search(lst, value):
    for i in lst:
        if i == value:
            return True
    return False


# binary search : O(log(n))
# @Assumes that data is sorted
def binary_search(lst, value):
    left = 0
    right = len(lst)-1

    while left <= right:
        middle = left + (right-left)/2 # prevet overflow
        print "middle = %s" % middle
        if lst[middle] < value:
            left = middle + 1
        elif lst[middle] > value:
            right = middle - 1
        else:
            return True
    return False

# binary search : O(log(n))
# @Assumes that data is sorted
def binary_search(lst, value, left, right):
    if left > right:
        return False
    middle = left + (right-left)/2 # prevent overflow
    if lst[middle] < value:
        return binary_search(lst, value, middle+1, right)
    elif lst[middle] > value:
        return binary_search(lst, value, left, right-1)
    else:
        return True


# hash search : O(1), load factor affects the bigO while collison happens

lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print sequencial_search(lst, 3)
# print sequencial_search(lst, 13)
lst.sort()
# print binary_search(lst, 3)
# print binary_search(lst, 13)
print binary_search(lst, 3, 0, len(lst)-1)
print binary_search(lst, 13, 0 , len(lst)-1)