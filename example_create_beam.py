# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:51:32 2022

@author: mrsup
"""

from Beam import *

newBeamProp = { 
        "material" : {
                "name" : "steel",
                "E" : 210.0e9,
                "rho" : 0.3,
                "symmetry" : "isotropic"
            },
        "length" : 1.0,
        "cross_section" : {
                "name" : "rectangular",
                "dimensions" : [0.2, 0.15],
                
            }
    }

newBeam = Beam(**newBeamProp)

