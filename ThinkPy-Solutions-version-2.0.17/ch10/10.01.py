#
# Exercise 1
#
# Write a function called nested_sum that takes a nested list
# of integers and add up the elements from all of the nested lists.
# Sometimes you want to traverse one list while building another.
# For example, the following function takes a list of strings and
# returns a new list that contains capitalized strings:
#   def capitalize_all(t):
#       res = []
#       for s in t:
#           res.append(s.capitalize())
#       return res
#
# res is initialized with an empty list; each time through
# the loop, we append the next element. So res is another
# kind of accumulator.
# An operation like capitalize_all is sometimes called a map
# because it maps a function (in this case the method
# capitalize) onto each of the elements in a sequence.
#

def nested_sum(n_list):
    total = 0
    for n in n_list:
        try:
            total += sum(n)
        except TypeError:
            print "some elements in the list is not nested, so skip."
    return total


my_list = [ [], [1,1,1], 2, [1,1,1], 3.5, 'hello', [1.1,1.1,1.1] ]
print nested_sum(my_list)