#
# Exercise 9
# Starting with this diagram, execute the program on paper,
# changing the values of i and j during each iteration.
# Find and fix the second error in this function.


def is_reverse_my(word1, word2):
    '''compare two words and return True if one of the words is the reverse of the other'''

    if len(word1) != len(word2):
        return False
    else:
        index = len(word2) - 1
        for w in word1:
            # print index # for debugging
            if w != word2[index]:
                return False
            else:
                index -= 1

        return True

# print is_reverse_my('pots', 'stop')


# text book version
def is_reverse(word1, word2):
    # guardian pattern
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j > -1:
        print i, j # for debugging
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1

    return True

print is_reverse('pots', 'stop')