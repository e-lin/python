#
# Exercise 4
# Modify reverse_lookup so that it builds and returns a list
# of all keys that map to v, or an empty list if there are none.
#
def histogram(s):
    d = {}
    for c in s:
        if 0 == d.get(c, 0):
            d[c] = 1
        else:
            d[c] += 1
    return d

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup2(d, v):
    rtn_list = []
    for k in d:
        if d[k] == v:
            rtn_list.append(k)
    return rtn_list



if "__main__" == __name__:
    h = histogram('parrotmm')
    print reverse_lookup2(h, 2)
