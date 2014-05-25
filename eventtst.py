import gzip
import numpy as np

import parse_pdb as p
from eventdispatcher import EventDispatcher, Event

atmrec = [
    ('resnum', 'i4'),
    ('name', '<U4'),
    ('altloc', 'U1'),
    ('coord', 'f4',(3)),
    ('occ', 'f4'),
    ('b', 'f4'),]

resrec = [
    ('cid', 'U1'),
    ('resnum', 'i4'),
    ('restyp', '<U3'),
    ('inscod', 'U1'),
    ('het', 'b')]

class Model:
    def __init__(self, name):
        self.name = name
        self.atoms = []
        self.residues = []
        self.chains = []

    def __repr__(self):
        return "<Model {} chains: {}>".format(self.name, len(self.chains))
    #.
#.

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


class StructureParser:
    def __init__(self):
        self.mode = 'mini'
        self.models = []
        self.model = None

    def _new_model(self, name):
        model = Model(name)
        self.models.append(model)
        self.model = model
        self.atoms = self.model.atoms
        self.residues = self.model.residues
        self.chains = self.model.chains

        # Status member variables
        self.current_chain = "%"
        self.resct = 0
        self.atmct = 0
        self.current_residue = -999

    def on_atom(self, event):
        if self.model is None:
            # This happens in entries without an explicit MODEL
            # statement, create model 1
            self._new_model(1)
        #.

        t = p.atom(event.data)
        self.atmct += 1
        resnum = t[7]

        # Pack the atom record
        atmnam = t[2]+t[3]
        atmnam = atmnam.strip()

        #      resnum, atmnam, altloc, coords, occ,  bfactor
        atm = (resnum, atmnam, t[4], t[9:12], t[12], t[13])

        if self.current_residue != resnum:
            # Pack residue record
            #     cid, resnum, restyp, inscod, hetatm)
            res = (t[6], resnum, t[5], t[6], t[0])
            self.residues.append(np.array(res,dtype=resrec))
            self.current_residue = resnum
            self.resct += 1
        #.
        self.atoms.append(np.array(atm,dtype=atmrec))
    #.

    def on_end(self, event):
        raise StopIteration

    def on_model(self, event):
        nmodel = int(event.data[10:14])
        if self.mode == 'mini' and nmodel > 1:
            raise StopIteration
        self._new_model(nmodel)
        #.

    def finish(self):
        # OBS Need to terminate chain, residue, etc. defs
        print ("Finish...")
        cid_prev = "%"
        for r in self.residues:
            pass
        #.

#.


def pdbparser(fnam, mode='mini'):
    handler = StructureParser()
    handler.mode = mode

    # Create and instance of event dispatcher
    dispatcher = EventDispatcher()
    dispatcher.add_event_listener("ATOM", handler.on_atom)
    dispatcher.add_event_listener("HETATM", handler.on_atom)
    dispatcher.add_event_listener("MODEL", handler.on_model)
    dispatcher.add_event_listener("END", handler.on_end)

    # sniff first two bytes
    fd = open(fnam, "rb")
    sig = fd.read(2)
    fd.close()
    if sig == b'\x1f\x8b':
        fd = gzip.open(fnam, 'rt')
    else:
        fd = open(fnam, 'rt')
    #.

    # This is the event loop
    while True:
        try:
            line = next(fd)
            key = line[0:6].strip()
            ev = Event(key, data=line)
            dispatcher.dispatch_event(ev)
        except StopIteration:
            handler.finish()
            break
    #.

    # Tear down event dispatcher
    dispatcher.remove_event_listener("ATOM", handler.on_atom)
    dispatcher.remove_event_listener("HETATM", handler.on_atom)
    dispatcher.remove_event_listener("END", handler.on_end)

    return StructureHandler(handler.models)
#

if __name__ == "__main__":

    fnam = "1psr.pdb.gz"
    fnam = "1ot6.pdb.gz"
    fnam = "Phn4_1_7A_refine_16.pdb"
    fnam = "4q29.pdb.gz"
    s = pdbparser(fnam)
#.
