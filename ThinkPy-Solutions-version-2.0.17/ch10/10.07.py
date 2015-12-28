#
# Exercise 7
# Two words are anagrams if you can rearrange the letters
# from one to spell the other. Write a function called
# is_anagram that takes two strings and returns True if
# they are anagrams.
#
def is_anagram(word_a, word_b):
    word_a_lst = list(word_a)
    word_b_lst = list(word_b)

    word_a_lst.sort()
    word_b_lst.sort()

    # return word_a_lst.sort() == word_b_lst.sort() =====> WRONG!!! list.sort() return NONE, so you will always get Ture (as NONE == NONE) here.
    return word_a_lst == word_b_lst

print is_anagram('abcd','cdaa')
print is_anagram('abcd','cbda')

