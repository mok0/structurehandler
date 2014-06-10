# The Model class represents a model, which is the top-most structural
# container, equivalent to the MODEL entity of the PDB file. A model
# can contain several chains.

class Model:
    def __init__(self, name, residues, atoms):
        self.name = name
        self.residues = residues # __class__.__name__ == 'ndarray'
        self.atoms = atoms
        self.chains = {}
        # Populate self.chains, an index into the residues array.
        cid_current = self.residues['cid'][0]
        res_beg = 0
        resct = -1
        for r in self.residues:
            resct += 1
            cid = r['cid']
            if cid != cid_current:
                cid_current = cid
                self.chains[cid] = (cid, res_beg, resct)
                res_beg = resct
            #.
        #.
    #.

    def __repr__(self):
        s = "<ModelList {} chains: {} residues: {} atoms: {}>"
        return s.format(self.name, len(self.chains), len(self.residues), len(self.atoms))

    #.
#.
