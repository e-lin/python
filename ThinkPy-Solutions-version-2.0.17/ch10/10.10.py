#
# Exercise 10
# Write a function that reads the file words.txt and builds a list
# with one element per word. Write two versions of this function,
# one using the append method and the other using the idiom t = t + [x].
# Which one takes longer to run? Why?
#
# Hint: use the time module to measure elapsed time.
# Solution: http://thinkpython.com/code/wordlist.py.
#
import time

def make_word_list_1():
    f = open('words.txt','r')
    word_list = []

    t_start = time.time()

    for line in f:
        w = line.strip()
        word_list.append(w)

    t = time.time() - t_start

    print len(word_list)
    print word_list[:10]
    print "time elapsed: ", t, 'seconds'


def make_word_list_2():
    f = open('words.txt','r')
    word_list = []

    t_start = time.time()

    for line in f:
        w = line.strip()
        word_list = word_list + [w]

    t = time.time() - t_start

    print len(word_list)
    print word_list[:10]
    print "time elapsed: ", t, 'seconds'


make_word_list_1()
make_word_list_2()

# ---result---
# list + operator is slower than list append
# reference: http://stackoverflow.com/questions/20816600/best-and-or-fastest-way-to-create-lists-in-python
