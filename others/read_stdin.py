import sys

line_count = 0

def program_logic(line):
    global line_count
    line_count += 1
    print str(line_count) + ': ' + line.rstrip()

def read_from_stdin():
    global line_count
    for line in sys.stdin:
        program_logic(line)

def prompt_user():
    print 'Type "quit" to exit.'
    while (True):
        line = raw_input('PROMPT> ')
        if line == 'quit':
            sys.exit()
        program_logic(line)

if __name__ == "__main__":
    if '-' in sys.argv:
        read_from_stdin()
    else:
        prompt_user()