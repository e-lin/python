#
# Exercise 2
# In this example, ties are broken by comparing words, so words with the same
# length appear in reverse alphabetical order. For other applications you might
# want to break ties at random. Modify this example so that words with the same
# length appear in random order. Hint: see the random function in the random module.
# Solution: http://thinkpython.com/code/unstable_sort.py.
#
import random

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse = True)

    res = []
    for length, word in t:
        res.append(word)
    return res


def sort_by_length_random(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))

    t.sort(reverse = True)

    res = []
    for lenght, _, word in t:
        res.append(word)
    return res



if "__main__" == __name__:
    word_list = ['hardy', 'day', 'dad', 'happy', 'whatagreatday']
    print sort_by_length_random(word_list)
