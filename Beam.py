# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 15:04:27 2022

@author: mrsup
"""
import numpy as np


class Material():
    # --> TODO, vikhult, create subclasses for example isotropic materials
    
    def __init__(self, **kwargs):
        
        if len(kwargs) > 0:
            self.properties = {
                "name" : None,
                "rho" : None,
                "E" : None,
                "symmetry" : None
            }
            self.alter_properties(**kwargs)
            
    def report_properties(self):
        rpt_ = " === PROPERTIES ==="
        for k, v in self.properties.items():
            rpt_ += "{0:>10s} : {1:<}".format(k, v)
        return rpt_

    def alter_properties(self,**kwargs):
        rpt_ = ""
        
        # look through the properties and exchange the valid ones
        for k, v in kwargs.items():
            try:
                self.properties[k] = v
                rpt_ += "Property {} set to {} \n".format(k, v)
            except: 
                KeyError(
                    "Property not listed for the material"
                    )
        
        print(rpt_)


    def get_property(self, prop):
            try:
                return self.properties[prop]
            except: 
                KeyError(
                    "Property not listed for the material"
                    )

    # def get_E(self):
    #     return self.E
    
    # def set_E(self, **kwargs):
    #     self.E = kwargs["E"]
    
    # def get_rho(self):
    #     return self.rho
    
    # def set_rho(self, new_rho):
    #     self.rho = new_rho
    
    # def get_name(self):
    #     return self.name
    
    # def set_name(self, new_name):
    #     self.name = new_name
    

class Cross_section():
    def __init__(self,**kwargs):
        self.properties = {
            "name" : None,
            "valid_cross_sections" : ["rectangular"],
            "dimensions" : None,
            "I_ij" : None
        }
        self.alter_properties(**kwargs)
        self.properties["I_ij"] = self.calculate_mom_area_inertia()
        
                    
    def alter_properties(self,**kwargs):
        rpt_ = ""
        
        # look through the properties and exchange the valid ones
        for k, v in kwargs.items():
            try:
                self.properties[k] = v
                rpt_ += "Property {} set to {} \n".format(k, v)
            except: 
                KeyError(
                    "Property not listed for the cross section"
                    )
        
        print(rpt_)
                
                
    def calculate_mom_area_inertia(self):
        if self.properties["name"] == "rectangular":
            "see https://mathworld.wolfram.com/AreaMomentofInertia.html"
            a = self.properties["dimensions"][0]
            b = self.properties["dimensions"][1]
            I_ij = np.array([[1 / 12 * a * b**3, 0], [0, 1 / 12 * a**3 * b]])
            return I_ij
        else:
            raise NotImplementedError(
                "The provided cross section lacks this functionality"
                )


class Beam():  
    def __init__(self, **kwargs):
        self.properties = {
            "material" : None,
            "length" : None,
            "cross_section" : None
        }
        if len(kwargs) > 0:
            self.alter_properties(**kwargs)
        else:
            pass
    
    
    # def set_material(self, **kwargs):
    #     self.material.alter_properties(**kwargs)
        
    def alter_properties(self, **kwargs):
        rpt_ = ""
    
        # look through the properties and exchange the valid ones
        for k, v in kwargs.items():
            if k == "material":
                self.properties[k] = Material(**(kwargs[k]))
            elif k == "cross_section":
                self.properties[k] = Cross_section(**(kwargs[k]))
            else:
                try:
                    self.properties[k] = v
                    rpt_ += "Property {} set to {} \n".format(k, v)
                except: 
                    KeyError(
                        "Property not listed for the material"
                        )
        
        print(rpt_)
        
        
    def report_properties(self):
        rpt_ = " === PROPERTIES ==="
        for k, v in self.properties.items():
            if k == "material":
                pass
            elif k == "cross_section":
                pass
            else:
                rpt_ += "{0:>10s} : {1:<}".format(k, v)
        return rpt_