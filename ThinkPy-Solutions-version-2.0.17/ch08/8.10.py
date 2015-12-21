#
# Exercise 10
# A string slice can take a third index that specifies the step size;
# that is, the number of spaces between successive characters. A step
# size of 2 means every other character; 3 means every third, etc.
#
#   >>> fruit = 'banana'
#   >>> fruit[0:5:2]
#   'bnn'
#
# A step size of -1 goes through the word backwards, so the slice [::-1]
# generates a reversed string.
# Use this idiom to write a one-line version of is_palindrome from Exercise 6.
#
#
#
# A palindrome is a word that is spelled the same backward and forward,
# like noon and redivider. Recursively, a word is a palindrome if
# the first and last letters are the same and the middle is a palindrome.
#
def is_reverse(word1, word2):
    '''compare two words and return True if one of the words is the reverse of the other'''
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j > -1:
        # print i, j # for debugging
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1

    return True


def is_palindrome_my(word):
    if len(word) == 0:
        print "empty string."

    # if not isinstance(word, str)
    if not isinstance(word, basestring):
        print "not a string"

    if len(word) % 2 == 0:
        # even length
        word1 = word[:len(word)/2]
        word2 = word[len(word)/2:]
    else:
        # odd length
        word1 = word[:len(word)/2]
        word2 = word[len(word)/2 + 1:]

    return is_reverse(word1, word2)


# print is_palindrome_my('noon')
# print is_palindrome_my('redivider')
# print is_palindrome_my('nood')
# print is_palindrome_my('redivixer')


# version 2
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    while len(word) > 0:
        if first(word) == last(word):
            word = word[1:len(word)-1]
            is_palindrome(word)
        else:
            return False
    return True


# print is_palindrome('noon')
# print is_palindrome('redivider')
# print is_palindrome('nood')
# print is_palindrome('redivixer')



# version 3 (one-line version)
def is_palindrome_oneline(word):
    length = len(word)

    w1 = word[:length/2] # first half of word
    if length % 2 == 0:
        w2 = word[length/2:] # last half
    else:
        w2 = word[length/2 + 1:] # last half

    # if the reversed of w1 equals to w2, palindrome true
    if w1[::-1] == w2:
        return True
    else:
        return False


# print is_palindrome_oneline('noon')
# print is_palindrome_oneline('redivider')
# print is_palindrome_oneline('nood')
# print is_palindrome_oneline('redivixer')


# one-line verion answer
def is_palindrome_answer(word):
    return word == word[::-1]

print is_palindrome_answer('noon')
print is_palindrome_answer('redivider')
print is_palindrome_answer('nood')
print is_palindrome_answer('redivixer')




