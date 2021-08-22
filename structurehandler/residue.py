import collections
from .atom import Atom
from .deprecated import deprecated

class Residue(collections.OrderedDict):
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

    @deprecated
    def child_list(self):
        return self.atoms

    @deprecated
    def child_dict(self):
        return {k: v for k,v in self.items()}
    #.

    # Special methods

    def __repr__(self):
        return "<Residue {} ({})>".format (self.name, self.type)
    #.
#.

