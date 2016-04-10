#
# codejam contest
# https://code.google.com/codejam/contest/6254486/dashboard#s=p2
#
import string, math
digs = string.digits + string.letters

def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


def find_next_polite_number(n, divisor):
    for i in xrange(2, int(n ** .5) , 1):
        p_number = n / i

        if (n % i) == 0:
            if not i in divisor:
                divisor.append(i)
            return i
    return n

def gen_base_num(jam):
    return [int(int2base(int(jam, base), 10)) for base in xrange(2, 11, 1)]

def gen_jamcoin(length, find_count):
    l = length - 1
    s = 2 ** length
    jams = []
    for c in xrange((2 ** l) + 1, s, 1):
        jam = bin(c)[2:]
        if len(jams) < find_count and jam[len(jam) - 1] != '0':
            basesNum = gen_base_num(jam)
            divisor = []
            valid = True
            for i in xrange(len(basesNum)):
                num = find_next_polite_number(basesNum[i], divisor)
                if num == 1 or num == basesNum[i]:
                    valid = False
                    break
                else:
                    basesNum[i] = num
            if valid:
                jams.append((jam, basesNum))
    return jams

def load_input(filename = None):
    if not filename:
        return
    line_buffer = None

    with open(filename, 'r+') as f:
        line_buffer = f.read().splitlines()
    f.close()
    return line_buffer

import sys

def main(argv):
    if not argv:
        filename = __file__
        lines = ['1', '16 3']
    else:
        filename = argv[0]
        lines = load_input(filename + '.in')
    f = open(filename + '.out', 'w+')

    for i in xrange(int(lines[0])):
        N, J = map(str, lines[i + 1].split(' '))
        jamcoins = gen_jamcoin(int(N), int(J))
        s = 'Case #%d:\n' % (i+1)

        if jamcoins:
            for j in xrange(len(jamcoins)):
                s += ('%s %s\n' % (jamcoins[j][0], ' '.join(str(jam) for jam in jamcoins[j][1])))
        f.writelines(s)
        print '%s' % s
    f.close()

if __name__ == '__main__':
    main(sys.argv[1:])