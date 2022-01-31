#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Init file"""
from .pygcc_utils import *
from .read_db import db_reader
from .water_eos import iapws95, ZhangDuan, water_dielec, readIAPWS95data, convert_temperature
from .species_eos import heatcap, heatcapusgscal, supcrtaq, heatcap_Berman, Element_counts
from .solid_solution import solidsolution_thermo
from .clay_thermocalc import calclogKclays, MW

# read version from installed package
from importlib_metadata import version
__version__ = version("pygcc")


