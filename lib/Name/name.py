import sys

print "name: sys.path[0]:   ", sys.path[0]
print "name: sys.path.last:   ", sys.path

class Name:
    """A Name class"""
    name = "no name"

    def __init__(self):
        self.name = "init name"

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

