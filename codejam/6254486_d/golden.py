#
# code jam
# https://code.google.com/codejam/contest/6254486/dashboard#s=p3
#
# solution:
# see 0 as gold exist and 1 as gold not exist.
# we want to find positions that all numbers are not all 1.
# e.g., [0, 1, 0], [1, 1, 0] is ok. [1, 1, 1] means no golds.
#
import itertools

def add_layer(a_binary, C, ori_tile, gg_tile):
    """
    add layer for building complexity fractiles
    """
    for i in range(C-1):

        extend_tile = ()
        for tt in a_binary:
            if tt == 0: # G(gold exist)
                extend_tile += gg_tile
            elif tt == 1: # L(gold not exist)
                extend_tile += ori_tile

        a_binary = extend_tile
    return a_binary

def perms(n):
    if not n:
        return

    for i in xrange(2**n):
        s = bin(i)[2:]
        s = "0" * (n-len(s)) + s
        yield s

# print list(perms(5))

def build_fractiles(K, C):
    """ build a dict that key represents a tuple of 0 and 1 (the fractiles).
    and value represents the position of 1 showed up in the list
    e.g., {(0, 0, 1):[3], (1, 1, 0):[1,2]}
    """
    complexity_list = list()
    fractiles = dict()
    binary_list = list(itertools.product([0, 1], repeat=K)) # http://stackoverflow.com/questions/14931769/how-to-get-all-combination-of-n-binary-value
    # binary_list = list(perms(K))

    # print 'binary_list ======> '
    # print binary_list

    if C >= 2:
        # build complexity fractiles
        for b in binary_list:
            ori_tile = tuple(b)
            gg_tile = (0,)* len(ori_tile)

            complexity_binary = add_layer(tuple(b), C, ori_tile, gg_tile)
            # print 'complexity_binary ====> '
            # print complexity_binary
            complexity_list.append(complexity_binary)
    elif C == 1:
        complexity_list = binary_list

    for c in complexity_list:
        no_gold_pos = [ idx+1 for idx, cc in enumerate(c) if cc == 1 ] # flag position of L(gold not exist)
        fractiles[c] = no_gold_pos

    return fractiles

def pick_tiles(S, fractiles):
    """choose the most flag that enables as the pick-up
    baseline ($LLLLLLLLL)
    """
    # http://stackoverflow.com/questions/21839208/dictionary-with-lists-as-values-find-longest-list
    max_key, max_value = max(fractiles.items(), key = lambda x: len(set(x[1])))

    pickup_list = list(max_value)
    cmp_lists = list()
    pick_str_rtn = str()

    tmp_lists = fractiles.values()
    tmp_lists.remove(pickup_list)

    # stringlize the fractiles.values()
    for C in tmp_lists:
        cmp_str = ''.join(str(c) for c in C)
        cmp_lists += [cmp_str]

    # print 'fractiles: '
    # print fractiles
    # print 'fractiles.values(): '
    # print fractiles.values()
    # print 'pick up list: '
    # print pickup_list
    # print 'cmp_list: '
    # print cmp_lists

    for s in range(1, S+1):
        # print ('Round %d: ' % s)
        for pick in itertools.combinations(pickup_list, s): # http://stackoverflow.com/questions/464864/python-code-to-pick-out-all-possible-combinations-from-a-list
            # print pick
            # stringlize the pick(tuple)
            pick_str = ''.join(str(p) for p in pick)

            # if pick_str be partially same with c_str. http://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
            if not any(pick_str in c_str for c_str in cmp_lists):

                # insert space to retrun
                for i in range(len(pick_str)):
                    pick_str_rtn += pick_str[i]
                    pick_str_rtn += ' '

                return pick_str_rtn[:len(pick_str_rtn)-1]

    return 'IMPOSSIBLE'


def read_file(filename):
    with open(filename) as fd:
        input_list = fd.read().splitlines()

    return input_list

import sys

def main(argv):
    if not argv:
        print "Enter filename."
        sys.exit()

    filename = argv[0]
    input_list = read_file(filename + '.in')
    # f = open(filename + '.out', 'w+')

    T = int(input_list[0]) # the number of cases

    for t in range(1, T+1):

        paras = input_list[t].split(' ')
        K = int(paras[0])
        C = int(paras[1])
        S = int(paras[2])

        fractiles = build_fractiles(K, C)
        print fractiles
        picks = pick_tiles(S, fractiles)

        s = 'Case #%d: %s\n' % (t, picks)
        # f.write(s)
        print '%s' % s

    # f.close()


if __name__ == '__main__':
    main(sys.argv[1:])