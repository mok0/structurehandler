# The Chain represents a chain, describing the residues that share
# a chain identifier.

import collections
from .residue import Residue

class Chain(dict):
    def __init__(self, name, residues, atoms):
        self.name = name
        self.atoms = atoms
        self.store = collections.OrderedDict()
        for r in residues:
            atmlist = atoms[atoms['resnum'] == r[1]]
            self.store[r[1]] = Residue(r, atmlist)

    # Special methods

    def __repr__(self):
        s = "<Chain {}; residues: {}; atoms: {}>"
        return s.format(self.name, len(self.store), len(self.atoms))
    #.

    def __getitem__(self, key):
        return self.store[key]
    #.

    def __setitem__(self, key, value):
        self.store[key] = value
    #.

    def __delitem__(self, key):
        del self.store[key]
    #.

    def __iter__(self):
        return iter(self.store)
    #.

    def __len__(self):
        return len(self.store)
    #.

    def __contains__(self, key):
         "True if there is a child element with the given key."
         return key in self.store
    #.
#.
