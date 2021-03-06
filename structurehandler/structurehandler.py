class StructureHandler:
    def __init__(self):
        self.models = []
        self.model = None
        self.names = []


    @property
    def atoms(self):
        if self.model: return self.model.atoms
    #.

    @property
    def residues(self):
        if self.model: return self.model.residues
    #.

    @property
    def chains(self):
        if self.model: return self.model.chains
    #.

    def add(self, model):
        self.models.append(model)
        self.model = model
    #.

    def use_model(self, n):
        if n not in self.names:
            print ("Model", n, "does not exist")
            return
        #.
        self.model = self.names[n]
        self.atoms = self.model.atoms
        self.residues = self.model.residues
        #.
    #.
#.
