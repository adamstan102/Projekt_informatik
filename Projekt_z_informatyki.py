# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:31:01 2023

@author: User
"""

from math import sin, cos, sqrt, atan, atan2, degrees, radians, pi, tan
import numpy as np
from numpy import rad2deg, deg2rad, floor, array, append, linalg, dot, arccos


class Transformacje:
    def __init__(self, model: str = "wgs84"):
        if model == "wgs84":
            self.a = 6378137.0 # semimajor_axis
            self.b = 6356752.31424518 # semiminor_axis
        elif model == "grs80":
            self.a = 6378137.0
            self.b = 6356752.31414036
        elif model == "Krasowski":
            self.a = 6378245.0
            self.b = 6356863.01877      
        else:
            raise NotImplementedError(f"{model} Nie implementowany Model")
        self.flat = (self.a - self.b) / self.a
        self.ecc = sqrt(2 * self.flat - self.flat ** 2) 
        self.ecc2 = (2 * self.flat - self.flat ** 2) 
        
        
    def dms2deg(self, dms):
        d = dms[0]; m = dms[1]; s = dms[2]
        decimal_degree = d+m/60+s/3600
        
        return (decimal_degree)
    
    
    def deg2dms(self, decimal_degree):
        decimal_degree = decimal_degree / 3600
        dms = np.array([])
        st = np.floor(decimal_degree)
        np.append(dms, st)
        m = np.floor((decimal_degree - st)*60)
        np.append(dms, m)
        sek = (decimal_degree - st - m/60)*3600
        np.append(dms, sek)
        print(dms)
        
        return (dms)
    

    def xyz2plh(self, X, Y, Z, output = 'dec_degree'):
        r   = sqrt(X**2 + Y**2)   
        phi_prev = atan(Z / (r * (1 - self.ecc2)))    
        phi = 0
        while abs(phi_prev - phi) > 0.000001/206265:    
            phi_prev = phi
            N = self.a / sqrt(1 - self.ecc2 * sin(phi_prev)**2)
            h = r / cos(phi_prev) - N
            phi = atan((Z/r) * (((1 - self.ecc2 * N/(N + h))**(-1))))
        lam = atan(Y/X)
        N = self.a / sqrt(1 - self.ecc2 * (sin(phi))**2);
        h = r / cos(phi) - N       
        if output == "dec_degree":
            return degrees(phi), degrees(lam), h 
        elif output == "dms":
            phi = self.deg2dms(degrees(phi))
            lam = self.deg2dms(degrees(lam))
            
            return f"{phi[0]:02d}:{phi[1]:02d}:{phi[2]:.2f}", f"{lam[0]:02d}:{lam[1]:02d}:{lam[2]:.2f}", f"{h:.3f}"
        else:
            raise NotImplementedError(f"{output} - output format not defined")
            
    
    def Np(self, f):
        N = self.a / sqrt(1-self.ecc2*(sin(f)**2))
        
        return(N)
        
        
    def flh2XYZ(self, f,l,h):
        N = self.Np(f)
        X = (N+h)*cos(f)*cos(l)
        Y = (N+h)*cos(f)*sin(l)
        Z = (N*(1-self.ecc2)+h)*sin(f)
    
        return(X,Y,Z)

    
    def sigma(self, f):

        A0 = 1-(self.ecc2/4)-(3/64)*(self.ecc2**2)-(5/256)*(self.ecc2**3);
        A2 = (3/8)*(self.ecc2 + (self.ecc2**2)/4 + (15/128)*(self.ecc2**3));
        A4 = (15/256)*(self.ecc2**2 + 3/4*(self.ecc2**3));
        A6 = (35/3072)*self.ecc2**3;
        si = self.a*(A0*f - A2*sin(2*f) + A4*sin(4*f) - A6*sin(6*f));
    
        return(si)
  


    def xyz2flh(self,X, Y, Z):
        P = sqrt(X**2 + Y**2)
        f = np.arctan(Z/(P*(1 - self.ecc2)))
        while True:
            N = self.a/np.sqrt(1-self.ecc2*(np.sin(f))**2)
            h = P / cos(f) - N
            fp = f
            f = np.arctan(Z/(P* (1 - self.ecc2 * N / (N + h))))
            if abs(fp - f) < (0.000001/206265):
                break
        l = np.arctan2(Y, X)
        
        return(f, l, h)  

