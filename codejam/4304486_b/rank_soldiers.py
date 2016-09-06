def read_file(filename):
    with open(filename) as fd:
        input_list = fd.read().splitlines()

    print input_list
    return input_list



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
        N = int(input_list[t])
        # print 'N = %s ' % N
        last = 2*N-1
        # print 't = %s ' % t
        soldier_list = list()

        for i in range(t+1, t+1+last):
            soldier_list += str(input_list[i])
        t = last + 2
        print 't = %s ' % t
        print soldier_list

        # s = 'Case #%d: %d\n' % (t, flip_times)
        # f.write(s)
        # print '%s' % s

    # f.close()

if __name__ == '__main__':
    main(sys.argv[1:])