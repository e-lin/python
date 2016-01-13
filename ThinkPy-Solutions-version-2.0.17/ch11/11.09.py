#
# Exercise 9
# If you did Exercise 8 (ch10/10.08.py), you already have a function named has_duplicates
# that takes a list as a parameter and returns True if there is any object that appears
# more than once in the list.
# Use a dictionary to write a faster, simpler version of has_duplicates.
# Solution: http://thinkpython.com/code/has_duplicates.py.
#

def has_duplicates(ori_list):
    for i in range(len(ori_list)):
        if ori_list.count(ori_list[i]) > 1:
            return True
    return False

def has_duplicates_2(ori_list):
    """ A simple version """
    d = {}
    for i in ori_list:
        if i in d:
            return True
        d[i] = 'Shown'
    return False

def has_duplicates_3(ori_list):
    """ A faster version using set """
    return len(set(ori_list)) < len(ori_list)


if "__main__" == __name__:
    my_list = [1, 9, 8]
    print has_duplicates_3(my_list)
    my_list.append(1)
    print has_duplicates_3(my_list)