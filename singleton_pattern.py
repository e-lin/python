#
# Singleton Pattern
# Reference:
# http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Singleton.html
#

class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    instance = None

    def __init__(self, arg):
        if not OnlyOne.instance:
            print "Generate object only once"
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            print "Assign argument"
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)



def main():
    x = OnlyOne("sausage")
    print(x)
    y = OnlyOne("eggs")
    print(y)
    z = OnlyOne("spam")
    print(z)
    print(x)
    print(y)


if "__main__" == __name__:
    main()
