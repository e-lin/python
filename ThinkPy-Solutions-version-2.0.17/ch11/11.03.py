#
# Exercise 3
# Dictionaries have a method called keys that returns the keys
# of the dictionary, in no particular order, as a list.
# Modify print_hist to print the keys and their values in
# alphabetical order.
#
def histogram(s):
    d = {}
    for c in s:
        if 0 == d.get(c, 0):
            d[c] = 1
        else:
            d[c] += 1
    return d

def print_hist(h):
    key_list = h.keys()
    key_list.sort()
    for k in key_list:
        print k, h[k]



if "__main__" == __name__:
    h = histogram('brontosaurus')
    print_hist(h)