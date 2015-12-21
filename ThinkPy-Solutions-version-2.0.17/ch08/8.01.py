#
# Exercise 1
# Write a function that takes a string as an argument
# and displays the letters backward, one per line.
#

def print_backwards(string):
    length = len(string)
    idx = length - 1
    while idx > -1:
        print string[idx]
        idx -= 1

print_backwards("Peggy")


# another way to print backwards
def backwards(string):
    for i in string[::-1]:
        print i

backwards("Nick")