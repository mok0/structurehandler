# The Model class represents a model, which is the top-most structural
# container, equivalent to the MODEL entity of the PDB file. A model
# can contain several chains.


class Model:
    def __init__(self, name, residues, atoms):
        self.name = name
        self.residues = residues # __class__.__name__ == 'ndarray'
        self.atoms = atoms
        self.cids = set(residues['cid']) # set of chain ids found in model
        # self.chains = {}


        # for x in self.cids:

        #     # Populate self.chains, an index into the residues array.

        #     reslist = self.residues[self.residues['cid'] == x]
        #     atmlist = self.atoms[self.atoms['cid'] == x]
        #     self.chains[x] = Chain(x, reslist, atmlist)
        # #.
    #.

    def __repr__(self):
        s = "<Model {}; chains: {}; residues: {}; atoms: {}>"
        return s.format(self.name, len(self.cids), len(self.residues), len(self.atoms))
    #.
#.

from .chain import Chain

# The CRAtree object contains a hierachy of chain, residue and atom objects.

class CRAtree:
    def __init__(self, model):

        self.chains = {}

        for x in model.cids:

            # Populate self.chains, an index into the residues array.

            reslist = model.residues[model.residues['cid'] == x]
            atmlist = model.atoms[model.atoms['cid'] == x]
            self.chains[x] = Chain(x, reslist, atmlist)
        #.
    #.
#
