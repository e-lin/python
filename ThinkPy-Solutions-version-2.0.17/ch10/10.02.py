#
# Exercise 2
# Use capitalize_all to write a function named capitalize_nested
# that takes a nested list of strings and returns a new nested
# list with all strings capitalized.
#
# Another common operation is to select some of the elements from
# a list and return a sublist. For example, the following function
# takes a list of strings and returns a list that contains only the
# uppercase strings:
#
#   def only_upper(t):
#       res = []
#       for s in t:
#           if s.isupper():
#               res.append(s)
#       return res
#
# isupper is a string method that returns True if the string contains
# only upper case letters.
# An operation like only_upper is called a filter because it selects
# some of the elements and filters out the others.
#
# Most common list operations can be expressed as a combination of map,
# filter and reduce. Because these operations are so common, Python
# provides language features to support them, including the built-in
# function map and an operator called a list comprehension.
#

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(n_list):
    try:
        res_nested = []
        for n in n_list:
            res_nested.append(capitalize_all(n))
    except TypeError:
        print "some elements in the list is not nested, so skip."

    return res_nested


my_list = [ ['how','are','You','?'], ['I','am', 'OK.'], 2, 'hey' ]
print capitalize_nested(my_list)
