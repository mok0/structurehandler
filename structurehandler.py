class StructureHandler:
    def __init__(self, models):
        self.models = models
        self.names = {i.name:i for i in self.models}
        self.model = models[0]
        self.atoms = self.model.atoms
        self.residues = self.model.residues
        self.chains = self.model.chains

    def add(self, model):
        self.models.append(model)
        self.model = model

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
