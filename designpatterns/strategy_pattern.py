#
# Strategy Pattern
# Reference:
# http://stackoverflow.com/questions/963965/how-is-this-strategy-pattern-written-in-python-the-sample-in-wikipedia
#

class StrategyExample:
    def __init__(self, func = None):
        if func:
            self.execute = func

    def execute(self):
        print "Original Execution"

def executeReplacement1():
    print "Strategy 1"

def executeReplacement2():
    print "Strategy 2"

def executeReplacement3(self):
    print "Strategy 3"


### Dynamically add a method: pass function reference
strat0 = StrategyExample()
strat1 = StrategyExample(executeReplacement1)
strat2 = StrategyExample(executeReplacement2)

strat0.execute()
strat1.execute()
strat2.execute()

### Dynamically add a method: use the class name
StrategyExample.execute = executeReplacement3

strat0.execute()
strat1.execute()
strat2.execute()

### Dynamically add a method: binding to an instance only (using types)
import types

class StrategyExample2:
    def __init__(self, func = None):
        self.name = "Strategy Example 2"
        if func:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print self.name

def executeReplacement4(self):
    print self.name + " from execute 4"

def executeReplacement5(self):
    print self.name + " from execute 5"

strat0 = StrategyExample2()
strat4 = StrategyExample2(executeReplacement4)
strat4.name = "Strategy Example 4"
strat5 = StrategyExample2(executeReplacement5)
strat5.name = "Strategy Example 5"

strat0.execute()
strat4.execute()
strat5.execute()