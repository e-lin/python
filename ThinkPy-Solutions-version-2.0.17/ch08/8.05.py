#
# Exercise 5
# Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.
#

def count(string, letter):
    cnt = 0
    for l in string:
        if l == letter:
            cnt += 1
    return cnt

print count('ABAAAab', 'a')
