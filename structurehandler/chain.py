# The Chain represents a chain, describing the residues that share
# a chain identifier.

import collections
from .residue import Residue

class Chain(collections.OrderedDict):
    def __init__(self, name, residues, atoms):
        super(Chain, self).__init__()
        self.name = name
        self.atoms = atoms
        for r in residues:
            atmlist = atoms[atoms['resnum'] == r[1]]
            self[r[1]] = Residue(r, atmlist)

    @property
    def residues(self):
        return list(self.values())
    #.


    # Special methods

    def __repr__(self):
        s = "<Chain {}; residues: {}; atoms: {}>"
        return s.format(self.name, len(self), len(self.atoms))
    #.
#.
