import gzip
import numpy as np

atmrec_long = [
    ('serial', 'i4'),
    ('atmnam', '<U4'),
    ('altloc', 'U1'),
    ('restyp', '<U3'),
    ('cid', 'U1'),
    ('resnum', 'i4'),
    ('inscod', 'U1'),
    ('coord', 'f4',(3)),
    ('occ', 'f4'),
    ('b', 'f4'),
    ('segid', '<U4'),
    ('element', '<U2'),
    ('charge', '<U2')]

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
    ('inscod', 'U1'),]

def readpdb(fnam, model):
    # sniff first two bytes
    fd = open(fnam, "rb")
    sig = fd.read(2)
    fd.close()
    if sig == b'\x1f\x8b':
        fd = gzip.open(fnam, 'rt')
    else:
        fd = open(fnam, 'rt')
    #.
    thischain = "%"
    thisres = -999
    atmbeg = -1
    atmend = -1
#    resbeg = 0
#    resend = -1
    atmct = -1
    resct = -1
    atoms = []
    coords = []
    residx = []
    residues = []

    for line in fd:
        line = line.strip()
        key=line[0:6]
        if key[0:4] != "ATOM" and key[0:6] != "HETATM":
            continue
        #.

        serial_number = int(line[6:11])
        atmnam1 = line[12:14]
        atmnam2 = line[14:16]
        atmnam = atmnam1+atmnam2
        #atmnam = atmnam.rstrip().rjust(4)
        atmnam = atmnam.strip()
        altloc = line[16]
        restyp = line[17:20]
        restyp = restyp.strip()
        cid = line[21]
        resnum = int(line[22:26])
        inscod = line[26]  # insertion code
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        occ = float(line[54:60])
        bfactor = float(line[60:66])
        segid = line[72:76]
        element = line[76:78]
        charge = line[78:80]

        atmct += 1
        atmend = atmct
        resend = resct

        res = (cid, resnum, restyp, inscod)

        if thischain != cid:
#            if resend > 0:
#                cidx.append((resbeg, resend))
#            #.
#            resbeg = resct
            thischain = cid
            thisres = -999
            print ("New chain", thischain)
        #.

        if thisres != resnum:
            if atmend > 0:
                residx.append((atmbeg, atmend))
            #.
            atmbeg = atmct
            thisres = resnum
            residues.append(np.array(res,dtype=resrec))
            #print (thisres, end=" ")
            resct += 1
        #.
        atm = (resct, atmnam, altloc, (x, y, z), occ, bfactor,)
        atoms.append(np.array(atm,dtype=atmrec))
    #.
    print("Read", atmct, "atoms from", fd.name)
    fd.close()

    # Find chain limits
    cidx = []
    resbeg = 0
    cbeg = residues['cid'][resbeg]
    for i, cid in enumerate(residues['cid']):
        if cid != cbeg:
            cidx.append(resbeg,i)
            resbeg = i
            cbeg = cid
        #.
    #.


    return np.array(residues), np.array(atoms), residx, cidx
#.

# atoms['atmnam'][3:10]
# This works, too:
# atoms['atmnam'][list(range(3,10))]
# This does not work:
# atoms['atmnam'][range(3,10)]
# But this works:
# atoms['coord'][range(3,10)]
# More examples:
# residues['restyp']
# Using np.arange seems to work!
# residues[np.arange(0,10)]
# This gets all CA atoms (remember to fill with spaces)
# atoms[atoms['atmnam'] == b'  CA']

