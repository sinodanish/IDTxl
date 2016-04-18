# -*- coding: utf-8 -*-
"""
Tests the import of fiels in Fieldtrip format to IDTxl's Data class.
Note that ft2idtxl at the moment assumes that fieldtrip data are stored as .mat
files in MATLAB's v7.3 format (which specifies an hdf5 file)

Created on Mon Apr 18 10:53:07 2016

@author: wibral
"""

import numpy as np
from idtxl.data import Data
from idtxl.ft2idtxl import ft2idtxlconverter

ft2idtxlconverter("/home/wibral/unison/IDTxl/test/data/ABA04_Up_10-140Hz.mat",'data')
