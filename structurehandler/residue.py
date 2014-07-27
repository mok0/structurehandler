import collections
from .atom import Atom

class Residue(dict):
    """
    Class representing a residue. Behaves like a dictionary, 
    with atom names as keys.
    """
    def __init__(self, rrec, atmlist, *args, **kwargs):

        self.cid = rrec[0]
        self.num = rrec[1]
        self.type = rrec[2]
        self.inscod = rrec[3]
        self.het = rrec[4]
        self.store = collections.OrderedDict()
        for a in atmlist:
            self.store[a[2]] = Atom(a)
        #.
        self.xtra = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys
    #.

    @property
    def name(self):
        return "{}{}".format(self.cid, self.num)
    #.

    @property
    def atoms(self):
        return list(self.store.values())
    #.

    # Special methods

    def __repr__(self):
        return "<Residue {} ({})>".format (self.name, self.type)
    #.

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]
    #.

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value
    #.

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]
    #.

    def __iter__(self):
        return iter(self.store)
    #.

    def __len__(self):
        return len(self.store)
    #.

    def __contains__(self, key):
        "True if there is a child element with the given key."
        return self.__keytransform__(key) in self.store
    #.

    def __keytransform__(self, key):
        return key.upper()
    #.
#.

