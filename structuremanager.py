
class StructureManager:

    def __init__(self, mode="minimal", model=1):
        self.mode = mode
        self.model = model
        self.data = None
    #.

    def read(self, fnam):
        data = parser.readpdb(fnam, self.model)
        self.chains = data[0]
        self.residues = data[1]
        self.atoms = data[2]
    #.
#.
