# sequencial search : O(n)
def sequencial_search(alist, item):
    idx = 0
    found = False

    while idx < len(alist) and not found:
        if alist[idx] == item:
            found = True
            break
        idx += 1

    return found

# binary search : O(log(n))


# hash search : O(1), load factor affects the bigO while collison happens

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print sequencial_search(testlist, 3)
print sequencial_search(testlist, 13)