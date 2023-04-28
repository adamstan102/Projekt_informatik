# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:31:01 2023

@author: User
"""

from math import sin, cos, sqrt, atan, atan2, degrees, radians, pi, tan
import numpy as np
from numpy import rad2deg, deg2rad, floor, array, append, linalg, dot, arccos
import argparse


        if model == "wgs84":
            self.a = 6378137.0 # semimajor_axis
            self.b = 6356752.31424518 # semiminor_axis
        elif model == "grs80":
            self.a = 6378137.0
            self.b = 6356752.31414036
        elif model == "Krasowski":
            self.a = 6378245.0
            self.b = 6356863.01877
