
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
