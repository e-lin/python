#
# Exercise 1
# Write a function that reads the words in words.txt and stores them
# as keys in a dictionary. It does not matter what the values are.
# Then you can use the in operator as a fast way to check whether a
# string is in the dictionary.
#
with open("words.txt") as fd:
    word_list = fd.read().splitlines()

def build_dict():
    word_dict = {}
    for word in word_list:
        word_dict[word] = None
    return word_dict

def build_dict2():
    word_dict = { word:None for word in word_list }
    return word_dict

if "__main__" == __name__:
    # result = build_dict()
    result = build_dict2()
    print result