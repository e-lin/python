
class A(dict):
    def __getattr__(self, name):
       print "__getattr__"
       try:
            return self[name]
       except KeyError:
            return 'default'

a = A()
a.smokey
