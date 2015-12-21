# The following example shows how to use concatenation (string addition)
# and a for loop to generate an abecedarian series (that is, in alphabetical
# order). In Robert McCloskey book Make Way for Ducklings, the names of
# the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack.
# This loop outputs these names in order:
#
#   prefixes = 'JKLMNOPQ'
#   suffix = 'ack'
#
#   for letter in prefixes:
#       print letter + suffix
#
# The output is:
# Jack
# Kack
# Lack
# Mack
# Nack
# Oack
# Pack
# Qack
#
# Of course, that is not quite right because Ouack and Quack are misspelled.
# Exercise 2
# Modify the program to fix this error.
#

def abecedarian():
    prefixed = 'JKLMNOPQ'
    suffix = 'ack'

    for letter in prefixed:
        if letter == 'Q' or letter == 'O':
            print letter + 'u' + suffix
        else:
            print letter + suffix


abecedarian()