import collections
from .atom import Atom

class Residue(dict):
    """
    Class representing a residue. Behaves like a dictionary, 
    with atom names as keys.
    """
    def __init__(self, rrec, atmlist):

        self.cid = rrec[0]
        self.num = rrec[1]
        self.type = rrec[2]
        self.inscod = rrec[3]
        self.het = rrec[4]
        super(Residue, self).__init__()
        for a in atmlist:
            self[a[2]] = Atom(a)
        #.
        self.xtra = dict()
    #.

    @property
    def name(self):
        return "{}{}".format(self.cid, self.num)
    #.

    @property
    def atoms(self):
        return list(self.values())
    #.

    # Special methods

    def __repr__(self):
        return "<Residue {} ({})>".format (self.name, self.type)
    #.

    # def __getitem__(self, key):
    #     return self[key.upper()]
    # #.

    # def __setitem__(self, key, value):
    #     self[key.upper()] = value
    # #.

    # def __delitem__(self, key):
    #     del self[key.upper()]
    # #.

    # def __contains__(self, key):
    #     "True if there is a child element with the given key."
    #     return key.upper() in self
    # #.
#.

