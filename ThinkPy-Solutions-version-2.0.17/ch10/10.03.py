#
# Exercise 3
# Write a function that takes a list of numbers and returns
# the cumulative sum; that is, a new list where the ith element
# is the sum of the first i+1 elements from the original list.
# For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
#
def cumulative_sum(ori_list):
    rtn_list = []
    for i in range(len(ori_list)):
        j = 0
        cumulative_item = 0
        while not j > i:
            cumulative_item += ori_list[j]
            j += 1
        rtn_list.append(cumulative_item)
    return rtn_list


my_list = [ 5, 2, 8, 10 ]
print cumulative_sum(my_list)
