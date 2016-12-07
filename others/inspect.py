import inspect

class BaseClass(object):
    def __init__(self): pass

class TestClass(BaseClass):
    """docstring for TestClass"""
    def __init__(self):
        self.attr1 = 0
        self.attr2 = 365
        print "TestClass init."
    def foo(self):
        print "TestClass in foo."
    def foo2(self, a, b, c):
        print "TestClass in foo2, a+b+c = %s" % (a+b+c)


def main():
    t = TestClass()
    print "type of TestClass %s\nbase class is %s" % (type(t), type(t).__bases__)

    print "---list methods of object---"
    methods = inspect.getmembers(t, predicate=inspect.ismethod)
    for name, obj in methods:
        print "name: %s, obj: %s" % (name, obj)

    # dynamically invoke method
    f1 = getattr(t, 'foo')
    print "dynamically invoke %s" % f1
    f2 = getattr(t, 'foo2')
    print "dynamically invoke %s" % f2

if __name__ == '__main__':
    main()

