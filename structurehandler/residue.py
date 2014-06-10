import collections

class Residue(collections.OrderedDict):
    """
    Class representing a residue. Behaves like a dictionary, 
    with atom names as keys.
    """
    def __init__(self, cid, num, typ, inscod, *args, **kwargs):

        self.type = typ
        self.num = num
        self.cid = cid
        self.inscod = inscod
        self.idx = None
        self.store = dict()
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

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __contains__(self, key):
        "True if there is a child element with the given key."
        return self.__keytransform__(key) in self.store

    def __keytransform__(self, key):
        return key.upper()

#.

