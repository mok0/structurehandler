# This module contains functions to decode the various PDB
# records.

def atom (line):
    # Extract items from a PDB ATOM or HETATM record
    het = line[0:6] == "HETATM"
    atom = line[0:4] == "ATOM"
    if not het and not atom:
        return None
    #.
    try:
        serial_number = int(line[6:11])
    except:
        raise TypeError("Error decoding serial number: "+line[6:11])
    atmnam1 = line[12:14]
    atmnam2 = line[14:16]
    altloc = line[16]
    restyp = line[17:20]
    restyp = restyp.strip()
    cid = line[21]
    try:
        resnum = int(line[22:26])
    except:
        raise TypeError("Error decoding residue number: "+line[22:26])
    #.
    inscod = line[26]  # insertion code
    try:
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
    except:
        raise TypeError("Error decoding coordinates: "+line[30:54])
    #.
    try:
        occ = float(line[54:60])
    except:
        raise TypeError("Error decoding occupancy: "+line[54:60])
    #.
    try:
        bfactor = float(line[60:66])
    except:
        raise TypeError("Error decoding B factor: "+line[60:66])
    #.
    segid = line[72:76]
    element = line[76:78]
    charge = line[78:80]

    T = (het, serial_number, atmnam1, atmnam2, altloc, restyp, cid,
         resnum, inscod, x, y, z, occ, bfactor, segid, element, charge)

    return T
#.

def cryst1(line):
    if line[0:6] != "CRYST1":
        return None
    #.
    raise NotImplementedError("CRYST1")
#.
