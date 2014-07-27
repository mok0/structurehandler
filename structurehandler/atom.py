# The Atom object represents an atom


class Atom:
    def __init__(self, arec):
        self.cid = arec[0]
        self.resnum = arec[1]
        self.name = arec[2]
        self.altloc = arec[3]
        self.coord = arec[4]
        self.occ = arec[5]
        self.b = arec[6]

    def __repr__(self):
        s = "<Atom {}; {}; occ: {}; b: {}>"
        return s.format(self.name, str(self.coord), self.occ, self.b)
    #.
#.
