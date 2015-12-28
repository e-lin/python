#
# Exercise 6
# Write a function called is_sorted that takes a list as
# a parameter and returns True if the list is sorted in
# ascending order and False otherwise. You can assume (as
# a precondition) that the elements of the list can be
# compared with the relational operators <, >, etc.
#
# For example, is_sorted([1,2,2]) should return True
# and is_sorted(['b','a']) should return False.
#
def is_sorted(ori_list):
    # create a new list of a copy of ori_list
    sorted_list = ori_list[:]
    sorted_list.sort()

    if sorted_list == ori_list:
        return True
    else:
        return False

print is_sorted([1,2,2])
print is_sorted(['b','a'])