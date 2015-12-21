#
# Exercise 6
# Rewrite this function so that instead of traversing
# the string, it uses the three-parameter version of
# find from the previous section.
#
def find(word, letter, idx):
    index = idx
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def count(string, letter):
    cnt = 0
    idx = 0
    while idx < len(string):
        idx = find(string, letter, idx)
        if idx != -1:
            cnt += 1
        else:
            return cnt
        idx += 1
    return cnt

print count('ABAAAabaabBBbbb', 'a')
