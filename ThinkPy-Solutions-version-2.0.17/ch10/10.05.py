#
# Exercise 5
# Write a function called chop that takes a list, modifies
# it by removing the first and last elements, and returns None.
#
def chop(ori_list):
    if not len(ori_list) > 0:
        print "An empty list"
    else:
        del ori_list[0]
        del ori_list[len(ori_list)-1]
        print ori_list

chop([1,2,3,4,5])
chop([1,2])
chop([1,2,3])
chop([])
