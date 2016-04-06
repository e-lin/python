#
# Codejam practice
# https://code.google.com/codejam/contest/351101/dashboard#s=p1
#
import sys

def read_file(filename):
    with open(filename) as fd:
        input_list = fd.read().splitlines()
    return input_list


def reverse_word(r_list):
    return r_list[::-1]


def main(argv):
    if not argv:
        sys.exit()

    filename = argv[0]
    input_list = read_file(filename + '.in')

    N = int(input_list[0]) # the number of cases
    reverse_lists = list()

    for i in range(1, N+1):
        r_list = reverse_word(input_list[i].split(' '))
        reverse_lists += r_list
        print "Case #%d: %s" % (i, ' '.join(w for w in r_list))


if __name__ == '__main__':
    main(sys.argv[1:])
