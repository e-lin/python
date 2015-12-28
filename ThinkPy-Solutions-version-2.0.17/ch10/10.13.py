#
# Exercise 13
#
# Two words interlock if taking alternating letters from each
# forms a new word. For example, shoe and cold interlock to
# form schooled. Solution: http://thinkpython.com/code/interlock.py.
# Credit: This exercise is inspired by an example at http://puzzlers.org.
#
# 1. Write a program that finds all pairs of words that interlock.
# Hint: do not enumerate all pairs!
#
# 2. Can you find any words that are three-way interlocked; that is, every
# third letter forms a word, starting from the first, second or third?
#
with open('words.txt') as fd:
    word_list = fd.read().splitlines()


# word_dict = { word: None for word in word_list }

def split_word(word):
    word1 = word[::2]
    word2 = word[1::2]
    return (word1,word2)

def find_interlock(word):
    split = split_word(word)
    # if split[0] in word_dict and split[1] in word_dict:
    if split[0] in word_list and split[1] in word_list:
        print word, " = ", split[0], split[1]


if "__main__" == __name__:
    # for d in word_dict:
    for d in word_list:
        find_interlock(d)


### Using word_dict is faster that using word_list

# The in operator uses different algorithms for lists and dictionaries.
# For lists, it uses a search algorithm, as in Section 8.6. As the list
# gets longer, the search time gets longer in direct proportion.
# For dictionaries, Python uses an algorithm called a hashtable that has
# a remarkable property: the in operator takes about the same amount of
# time no matter how many items there are in a dictionary.
# I won’t explain how that’s possible, but you can read more about it
# at http://en.wikipedia.org/wiki/Hash_table.
