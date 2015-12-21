#
# Exercise 11
# The following functions are all intended to check
# whether a string contains any lowercase letters,
# but at least some of them are wrong. For each
# function, describe what the function actually
# does (assuming that the parameter is a string).
#

# 1 - BAD, it only checks the first char in the string.
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
print any_lowercase1('ABCDe')

# 2 - BAD, it checks the 'c' char, of course it will always return True.
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
print any_lowercase2('ABCDE')

# 3 - BAD, flag will get the indication of whether the last char is lowercase or not.
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
print any_lowercase3('aBCDE')

# 4 - OK
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
print any_lowercase3('ABCDE')

# 5 - OK
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
print any_lowercase3('ABCDE')
