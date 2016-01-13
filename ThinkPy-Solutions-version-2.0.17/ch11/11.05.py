#
# Exercise 5
# Read the documentation of the dictionary method setdefault
# and use it to write a more concise version of invert_dict.
# Solution: http://thinkpython.com/code/invert_dict.py.
#
def histogram(s):
    d = {}
    for c in s:
        if 0 == d.get(c, 0):
            d[c] = 1
        else:
            d[c] += 1
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict2(d):
    inverse = dict()
    for key in d:
        val = d[key]
        new_val = inverse.setdefault(val, None)

        if new_val == None:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_solution(d):
    inverse = {}
    for key, val in d.iteritems():
        inverse.setdefault(val, []).append(key)
    return inverse



if "__main__" == __name__:
    hist = histogram('parrot')
    print hist
    inverse = invert_dict_solution(hist)
    print inverse

