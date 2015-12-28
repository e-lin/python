#
# Exercise 4
# Write a function called middle that takes a list
# and returns a new list that contains all but the
# first and last elements. So middle([1,2,3,4])
# should return [2,3].
#
def middle(ori_list):
    return ori_list[1:len(ori_list)-1]

print middle([1,2,3,4,5,7])
print middle([1,2])
print middle([])