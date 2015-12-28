#
# Exercise 8
# The (so-called) Birthday Paradox:
# Write a function called has_duplicates that takes a list
# and returns True if there is any element that appears more
# than once. It should not modify the original list.
#
# If there are 23 students in your class, what are the chances
# that two of you have the same birthday? You can estimate this
# probability by generating random samples of 23 birthdays and
# checking for matches. Hint: you can generate random birthdays
# with the randint function in the random module.
#
# You can read about this problem at http://en.wikipedia.org/wiki/Birthday_paradox,
# and you can download my solution from http://thinkpython.com/code/birthday.py.
#
import random

def has_duplicates(ori_list):
    for i in range(len(ori_list)):
        if ori_list.count(ori_list[i]) > 1:
            return True
    return False

def random_bday(n):
    bday_list = []
    for i in range(n):
        bday = random.randint(1,365)
        bday_list.append(bday)
    return bday_list


def count_matches(students, simulations_times):
    count = 0
    for i in range(simulations_times):
        bday_list = random_bday(students)
        if has_duplicates(bday_list):
            count += 1
    return count


if "__main__" == __name__:

    students = 23
    simulations_times = 1000

    c = count_matches(students, simulations_times)
    print 'For %d times simulations' % simulations_times
    print 'with %d students' % students
    print 'there were %d times simulations with at least one match' % c


