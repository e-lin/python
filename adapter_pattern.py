#
# Adapter Pattern
# Reference:
# https://gist.github.com/pazdera/1145859
#


# Adaptee (source) interface
class EuropeanSocketInterface():
    def __init__(self): pass
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    def earth(self): pass


# Adaptee
class Socket(EuropeanSocketInterface):
    def __init__(self): pass

    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Target Interface
class USASocketInterface():
    def __init__(self): pass
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    def earth(self): pass


# Adpater
class Adapter(USASocketInterface):
    def __init__(self, __socket = None):
        self.__socket = __socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()

    def earth(self):
        return self.__socket.earth()



# Client
class ElectricKettle():
    def __init__(self, __power = None):
        self.__power = __power

    def boil(self):
        if self.__power.voltage() > 110:
            print "kettle on fire!"
        else:
            if self.__power.live() == 1 \
            and self.__power.neutral() == -1:
                print "Coffee time!"
            else:
                print "No power."



def main():
    # plug in
    socket = Socket()
    adapter = Adapter(socket)
    kettle = ElectricKettle(adapter)

    # make coffee
    kettle.boil()

    return 0


if "__main__" == __name__:
    main()



