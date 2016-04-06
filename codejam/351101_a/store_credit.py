#
# Google codejam practice
# https://code.google.com/codejam/contest/351101/dashboard#s=p0
#
import sys

case_num = 0 # number of cases
credit = 0 # the amount of credit
item = 0 # the number of items in the store
price = [] # the price list of items

def read_data(filename):
    with open(filename) as fd:
        input_list = fd.read().splitlines()

    case_num = int(input_list[0]) # convert string to int
    if case_num == 0:
        print("No cases in file. Exit the program")
        sys.exit()

    if case_num != (len(input_list)-1) / 3:
        print("Data loss. Please check file.")
        sys.exit()

    case_idx = 1
    for i in range(1, len(input_list), 3):
        credit = int(input_list[i])
        item = int(input_list[i+1])
        prices = input_list[i+2].split() # this should be a list, split str with space to a list

        assert len(prices) == int(item)
        assert isinstance(credit, int)
        assert isinstance(item, int)
        assert not isinstance(prices, basestring) # http://stackoverflow.com/questions/1835018/python-check-if-an-object-is-a-list-or-tuple-but-not-string

        (pick_item_idx, pair_item_idx) = pick_items(credit, item, prices)

        print("Case #%d: %d %d" % (case_idx, pick_item_idx+1, pair_item_idx+1))
        case_idx += 1


def pick_items(credit, item, prices):
    pick_item_idx = -1
    pair_item_idx = -1

    for i in range(len(prices)):
        pick_item = int(prices[i])
        pick_item_idx = i
        pair_item = credit - pick_item

        if str(pair_item) in prices[i+1:]:
            pair_item_indices = [ idx for idx, x in enumerate(prices) if x == str(pair_item) ] # http://stackoverflow.com/questions/6294179/how-to-find-all-occurrences-of-an-element-in-a-list

            if len(pair_item_indices) == 1:
                pair_item_idx = pair_item_indices[0]
            elif len(pair_item_indices) == 2:
                pair_item_idx = pair_item_indices[1]
            else:
                print("Wrong indices. Exit the program")
                sys.exit()

            # since Each test case will have exactly one solution, return here.
            return min(pick_item_idx, pair_item_idx), max(pick_item_idx, pair_item_idx)

    print("No matches in this case. Exit the program")
    sys.exit()


if "__main__" == __name__:
    read_data("A-large-practice.in")
