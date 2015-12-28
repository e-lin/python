#
# Exercise 12
# Two words are a reverse pair if each is the reverse of the other.
# Write a program that finds all the reverse pairs in the word list.
# Solution: http://thinkpython.com/code/reverse_pair.py.
#
def reverse_pair(word_list):
    pair_list = []
    for w in word_list:
        if word_list.count(w[::-1]) > 0:
            if pair_list.count(w) == 0:
                pair_list.append(w)

    return pair_list



if "__main__" == __name__:
    word_list = ['abcd','dcba','xyz','zyx','123','456','321','123']
    print reverse_pair(word_list)
