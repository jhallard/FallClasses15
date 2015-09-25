# Luca Mangiatroppo, famous programmer, one day comes home after a night of
# gastronomic excess.  With recollections from the dinner and the guests
# still dancing in his by now almost (but not entirely!) fuzzy mind, he sits down,
# and writes a succinct implementation of a well-known algorithm.
# Which algorithm is it?  What does the algorithm do?
# How would a more clear-headed computer scientists have named the Frittella class?

# To solve the problem, read the algorithm carefully, and look at the output
# of the unit tests.  You can run the tests by doing:

# python stramangiata.py

# Except for the funny names, this is a good implementation
# of a well-known and important algorithm.

# Some hints:

# If you have a list l = ['a', 'b', 'c', 'd'], then l[-1] indicates the last element
# of l, so l[-1] == 'd'.  By the way, l[0:2] = ['a', 'b']; read more about slices:
# https://docs.python.org/2/tutorial/introduction.html#lists
# You can add lists with the + sign.
# For a list x, len(x) is the number of elements in x.
# For a dictionary x, len(x) is the number of mappings in x.

# The "self" below refers to the object.  What in Java would be an object variable x,
# in Python it is self.x, that is, "the x of the object".
# Likewise, what in Java would be a method foo(), in python is defined
# def foo(self):
# so it gets the object as its first argument, and it is called by doing:
# self.foo()
# that is, calling foo() of the object.
# Read more about classes here: https://docs.python.org/2/tutorial/classes.html
# So the self.guests = {} in the __init__ method initializes the self.guests dictionary
# to empty when an object of the class Frittella is created.

# The implementation is very efficient, and is 34 lines of code.
# Study it, it contains... food for thought! :-)

import unittest

class Frittella(object):
    def __init__(self):
        self.guests = {}

    def _add_el(self, u):
        print "add_el : %s in guests? %s " % (str(u),str(u in self.guests))
        if u not in self.guests:
            self.guests[u] = None

    def _get_spaghetto(self, u):
        print "_get_g beginning : u = (%s)" % str(u)
        p = [u]
        while p[-1] is not None:
            print "appending to p : %s " % str(self.guests[p[-1]])
            p.append(self.guests[p[-1]])
        print "_get_g returning : %s " % str(p[:-1])
        return p[:-1]

    def _roll_spaghetto(self, s, r):
        print "_roll_spag : s = %s   :: r = %s " % (str(s), str(r))
        for u in s:
            if u != r:
                print "_roll_spag : %s != %s" % (str(u), str(r))
                self.guests[u] = r

    def add(self, u1, u2):
        print "add : u1 (%s) u2 (%s)" % (str(u1), str(u2))
        self._add_el(u1)
        self._add_el(u2)
        s1 = self._get_spaghetto(u1)
        s2 = self._get_spaghetto(u2)
        print "add : s1 = (%s)    s2 = (%s)" % (str(s1), str(s2))
        r1, r2 = s1[-1], s2[-1]
        if r1 != r2:
            print "add : r1 != r2 (%s != %s)" % (str(r1), str(r2))
            r = r1 if len(s1) > len(s2) else r2
            self._roll_spaghetto(s1 + s2, r)

    def pietanza(self):
        print "piet begin"
        lasagne = {}
        print "piet : guests.keys() = %s" % str(self.guests.keys())
        for u in self.guests.keys():
            r = self._get_spaghetto(u)[-1]
            lasagne[r] = lasagne.get(r, []) + [u]
        return lasagne.values()

    def mangia(self, l):
        for u, v in l:
            self.add(u, v)
        return self.pietanza()

class OraDiPranzo(unittest.TestCase):

    def test_mangiata(self):
        menu = [('joe', 'carl'), ('carl', 'hugo'), ('hugo', 'eric'), ('eric', 'carl'),
                ('annie', 'helen'), ('helen', 'annie'), ('rosa', 'carla'), ('luise', 'hanna'), ('hanna', 'carla')]
        frittella = Frittella()
        print "Mangiata:", frittella.mangia(menu)

    # def test_mangiatona(self):
        # menu = [('joe', 'carl'), ('carl', 'hugo'), ('hugo', 'eric'), ('eric', 'carl'),
                # ('rob', 'luca'), ('luca', 'annie'),
                # ('annie', 'helen'), ('helen', 'annie'), ('rosa', 'carla'), ('luise', 'hanna'), ('hanna', 'carla')]
        # frittella = Frittella()
        # print "Mangiatona:", frittella.mangia(menu)

if __name__ == '__main__':
    unittest.main()
