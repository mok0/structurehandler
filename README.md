# A Python module to parse PDB files

Efficient event driven parser


    from structurehandler.structureparser import pdbparser

`mode="mini"` is the default mode, reads only first model.


    s = pdbparser(fnam, mode="mini")

``` python

In [63]: s.residues
Out[63]:
array([('A', 2, 'MSE', ' ', 1), ('A', 3, 'ASN', ' ', 0),
       ('A', 4, 'ILE', ' ', 0), ('A', 5, 'ILE', ' ', 0),
...
       ('B', 396, 'HOH', ' ', 1), ('B', 397, 'HOH', ' ', 1)],
       dtype=[('cid', '<U1'), ('resnum', '<i4'), ('restyp', '<U3'), ('inscod', '<U1'), ('het', 'i1')])
```



## Hierachial interface

    from structurehandler.structureparser import pdbparser
    from structurehandler.cratree import CRAtree


    fnam = "1psr.pdb.gz"
    s = pdbparser(fnam, mode="mini")
    tree = CRAtree(s.model)
    chain = tree.chains['A']

    for ires in chain:
        res = chain[ires]
        print (ires, res)
        for a in res:
            atm = res[a]
            print (a, atm)







In [5]: res = chain[50]

In [6]: list(res.values())
Out[6]:
[<Atom N; [ -1.67799997  54.00799942  50.31299973]; occ: 1.0; b: 11.09000015258789>,
 <Atom CA; [ -2.52900004  54.73899841  49.43500137]; occ: 1.0; b: 11.930000305175781>,
 <Atom C; [ -2.37599993  54.36199951  47.98600006]; occ: 1.0; b: 10.930000305175781>,
 <Atom O; [ -2.91799998  55.07699966  47.11500168]; occ: 1.0; b: 13.520000457763672>]


In [7]: for k,v in res.items():
   ...:     print (k,v)
   ...:
N <Atom N; [ -1.67799997  54.00799942  50.31299973]; occ: 1.0; b: 11.09000015258789>
CA <Atom CA; [ -2.52900004  54.73899841  49.43500137]; occ: 1.0; b: 11.930000305175781>
C <Atom C; [ -2.37599993  54.36199951  47.98600006]; occ: 1.0; b: 10.930000305175781>
O <Atom O; [ -2.91799998  55.07699966  47.11500168]; occ: 1.0; b: 13.520000457763672>


A residue object acts like a dictionary, with atom names as keys:

´´´ python
In [8]: res['N']
Out[8]: <Atom N; [ -1.67799997  54.00799942  50.31299973]; occ: 1.0; b: 11.09000015258789>
´´´
