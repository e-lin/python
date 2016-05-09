#
# codejam contest
# https://code.google.com/codejam/contest/4314486/dashboard#s=p0&a=0
#

def read_file(filename):
    with open(filename) as fd:
        input_list = fd.read().splitlines()

    return input_list

def build_senators(party, number_list):
    """ return a dictionary that contains the party and the number of senators
    e.g., for case #1: {'A': 2, 'B': 2}, case #2: {'A': 3, 'C': 2, 'B': 2}
    """
    senators = dict()

    for p in range(party):
        alphabet = chr(p + ord('A'))
        numbers = int(number_list[p])

        senators[alphabet] = numbers

    # print senators
    return senators

import math
def is_absolute_majority(senators):
    majority = sum(senators.values())
    # dictionary sum of values
    # http://stackoverflow.com/questions/4880960/sum-of-all-values-in-a-python-dict

    over_half = math.ceil(majority/2.0)
    for party in senators:
        if senators.get(party) >= over_half: return True
    return False

def rm_party(senators, party):
    """ remoe party if no senator in the party
    """
    if senators[party] == 0: del senators[party]
    return senators

def build_plan(senators):
    """ in each step pick one/two senators, and ensures that no party ever
    has an absolute majority.
    """
    plan = str()

    while len(senators) != 0:
        senators, p = pop(senators)
        plan += p
        plan += " "

    return plan[:-1] # kick the last space off

def pop(senators):
    senators_cpy = dict(senators)
    man = str()

    if len(senators_cpy) == 2:
        """
        if we start with two parties? Since the problem statement guarantees that
        no party begins with a majority, these parties must have equal numbers of
        senators. So, we can evacuate them in pairs, one from each party, until the
        evacuation is complete.
        """

        parties = list(senators_cpy.keys())
        # http://stackoverflow.com/questions/3545331/how-can-i-get-dictionary-key-as-variable-directly-in-python-not-by-searching-fr
        for party in parties:
            man += party
            senators_cpy[party] -= 1
            senators_cpy = rm_party(senators_cpy, party)
    else:
        """
        If we start with three or more parties and keep evacuating a single senator
        from the largest party in this way, then at some point, we must reach a step
        in which we go from three parties to two parties. These two remaining parties
        must have only one senator each. Since we just removed the one remaining senator
        from the third party, it must have been a largest party, so the other two can
        be no larger. So we can remove this last pair of senators in a single evacuation
        as a final step.
        """

        # pick one man to evacuate
        party = max(senators_cpy, key=senators_cpy.get)
        # party with the max value (number of ppl in the party)
        # http://stackoverflow.com/questions/3282823/get-key-with-the-least-value-from-a-dictionary

        man += party
        senators_cpy[party] -= 1
        senators_cpy = rm_party(senators_cpy, party)

    # print '----- start -------'
    # print senators_cpy
    # print man
    # print '=End='
    return senators_cpy, man

import sys

def main(argv):
    if not argv:
        print "Enter filename."
        sys.exit()

    filename = argv[0]
    input_list = read_file(filename + '.in')
    f = open(filename + '.out', 'w+')

    T = int(input_list[0]) # the number of cases

    for t in range(1, T+1):
        senators = build_senators(int(input_list[2*t-1]), list(input_list[2*t].split(" ")) )
            # space delimited string to list
            # http://stackoverflow.com/questions/4383082/python-regex-separate-space-delimited-words-into-a-list

        evacuate_plan = build_plan(senators)

        s = 'Case #%d: %s\n' % (t, evacuate_plan)
        f.write(s)
        print '%s' % s

    f.close()


if __name__ == '__main__':
    main(sys.argv[1:])