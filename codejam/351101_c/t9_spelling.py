#
# codejam practice
# https://code.google.com/codejam/contest/351101/dashboard#s=p2
#
def build_dict():
    tp_dict = {
                'a':'2', 'b':'22', 'c':'222',
                'd':'3', 'e':'33', 'f':'333',
                'g':'4', 'h':'44', 'i':'444',
                'j':'5', 'k':'55', 'l':'555',
                'm':'6', 'n':'66', 'o':'666',
                'p':'7', 'q':'77', 'r':'777', 's':'7777',
                't':'8', 'u':'88', 'v':'888',
                'w':'9', 'x':'99', 'y':'999', 'z':'9999',
                ' ':'0'
                }
    return tp_dict

def read_file(filename):
    with open(filename) as fd:
        input_list = fd.read().splitlines()

    return input_list


import sys

def main(argv):
    if not argv:
        print "Enter filename."
        sys.exit()

    tp_dict = build_dict()
    filename = argv[0]
    input_list = read_file(filename + '.in')
    f = open(filename + '.out', 'w+')

    N = int(input_list[0]) # the number of cases
    for i in range(1, N+1):
        sentence = str(input_list[i])

        tp_spelling = str()

        tp_spelling += tp_dict[sentence[0]] # 1st character\number of sentence.

        for char in range(1, len(sentence)):
            # if the current number (pick 1st.) equals to the previous number, add space.
            if tp_spelling.endswith( tp_dict[sentence[char]][0] ):
                tp_spelling += " "
                tp_spelling += tp_dict[sentence[char]]
            else:
                tp_spelling += tp_dict[sentence[char]]

        s = 'Case #%d: %s\n' % (i, tp_spelling)
        f.write(s)
        print '%s' % s

    f.close()


if __name__ == '__main__':
    main(sys.argv[1:])