'''
Your task is to define the following two methods for the intSet class:

Define an intersect method that returns a new intSet containing elements that
appear in both sets. In other words,

s1.intersect(s2)

would return a new intSet of integers that appear in both s1 and s2. Think
carefully - what should happen if s1 and s2 have no elements in common?

Add the appropriate method(s) so that len(s) returns the number of elements in
s.

Hint: look through the Python docs to figure out what you'll need to solve
this problem. https://docs.python.org/3.3/reference/datamodel.html
'''

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        """Returns an intSet of the common values between two intSets"""
        myset = intSet()
        for i in self.vals:
            if i in self.vals and i in other.vals:
                myset.insert(i)
        return myset
    
    def __len__(self):
        """Returns the length of an intSet"""
        return len(self.vals)

# establish instances of the class
s1 = intSet()
s2 = intSet()

# add values to the intSet to test
s1.insert(3)
s1.insert(1)
s2.insert(2)
s2.insert(3)

# testing
print(s1.intersect(s2))
print(len(s1))