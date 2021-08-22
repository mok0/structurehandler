# -*- coding: utf-8 -*-
#
# Distutils installation script
#


from distutils.core import setup
from structurehandler import __version__

setup(name="structurehandler",
      version=__version__,
      description="Python module for macromolecular structures",
      author="Morten Kjeldgaard",
      author_email="mok@bioxray.dk",
      url='https://github.com/mok0/structurehandler',
      license="GPL-3",
      package_dir={'structuremanager': 'structuremanager'},
      long_description="""Python module to parse PDB files 
and to manage models, chains, residues and atoms.""")
####

# 
