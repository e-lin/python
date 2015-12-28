#
# Exercise 9
# Write a function called remove_duplicates that takes a list
# and returns a new list with only the unique elements from
# the original. Hint: they do not have to be in the same order.
#
def remove_duplicates(ori_list):
    rtn_list = []
    for n in ori_list:
        if not n in rtn_list:
            rtn_list.append(n)

    return rtn_list

print remove_duplicates([1,1,2,5,3,5,4])
print remove_duplicates(['a','a',1,'b',2,'b'])