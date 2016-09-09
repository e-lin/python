#
# Python Decorator
# Reference:
# https://www.dotblogs.com.tw/rickyteng/archive/2013/11/06/126852.aspx
# http://python-3-patterns-idioms-test.readthedocs.org/en/latest/PythonDecorators.html
#


# ---------------------------
# Python Decorator Example 1
# ---------------------------
def logged(func):
    """A function prints the function name fof logging"""
    def with_logging(*args, **kwargs):
        print func.__name__ + " was called."
        return func(*args, **kwargs)
    return with_logging

@logged
def myFunction(num):
    return num + num

# @logged is exactly same with this: myFunction = logged(myFunction)
print myFunction(3)


# ---------------------------
# Easier way to describe @logged
# ---------------------------
def logged2(func):
    print func.__name__ + " was called."
    return func

@logged2
def myFunction2(num):
    return num * num

print myFunction2(5)


# ---------------------------
# Python Decorator Example 2
# ---------------------------
def makebold(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func() + "<b>"
    return wrapper

def makeitalic(func):
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "<i>"
    return wrapper

@makeitalic
@makebold
def htmlLink():
    return "hello world"

print htmlLink()


# ---------------------------
# Python Decorator Example 3
# ---------------------------
class entryExit():
    def __init__(self, func):
        print "Enter entry init."
        self.func = func
        print "Exit entry init."

    def __call__(self, *args):
        print "Enter " + self.func.__name__
        rtn = self.func(*args)
        print "Exit " + self.func.__name__
        return rtn

print "--- Decorator Start ---"
@entryExit
def hello(name):
    print "Inside hello()."
    return "Hi friend, " + name

print "--- Test Start ---"
print hello("Peggy")

