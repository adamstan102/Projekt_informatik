# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:31:01 2023

@author: User
"""

from math import sin, cos, sqrt, atan, atan2, degrees, radians, pi, tan
import numpy as np
from numpy import rad2deg, deg2rad, floor, array, append, linalg, dot, arccos
import argparse


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
    
     def fl2pl1992(self,f,l,l0=radians(19), m0 = 0.9993):
        b2 = self.a**2*(1 - self.ecc2)
        ep2 = (self.a**2 - b2)/b2
        dl = l - l0
        t = tan(f)
        n2 = ep2 * cos(f)**2
        N = self.a/np.sqrt(1-self.ecc2*(np.sin(f))**2)
        sigm = self.sigma(f)
        xgk = sigm + (dl**2/2) * N * sin(f)*cos(f)*(1 + (dl**2/12)*cos(f)**2*(5-t**2+9*n2+4*n2**2)+ ((dl**4)/360)*cos(f)**4*(61 - 58*t**2 + t**4 + 270*n2 - 330*n2*t**2))
        ygk = dl*N*cos(f)*(1+(dl**2/6)*cos(f)**2*(1 - t**2 + n2) + (dl**4/120)*cos(f)**4*(5 - 18*t**2 + t**4 + 14*n2 - 58*n2*t**2))
        x92 = xgk * m0 - 5300000
        y92 = ygk * m0 + 500000
        return x92,y92
    
    
     def fl2pl2000(self,f,l,m0= 0.999923):
        lama0=0 
        strefa = 0
        if l >np.deg2rad(13.5) and l < np.deg2rad(16.5):
            strefa = 5
            lama0 = np.deg2rad(15)
        elif l >np.deg2rad(16.5) and l < np.deg2rad(19.5):
            strefa = 6
            lama0 = np.deg2rad(18)
        elif l >np.deg2rad(19.5) and l < np.deg2rad(22.5):
            strefa =7
            lama0 = np.deg2rad(21)
        elif l >np.deg2rad(22.5) and l < np.deg2rad(25.5):
            strefa = 8
            lama0 = np.deg2rad(24)
        b2 = self.a**2*(1 - self.ecc2)
        ep2 = (self.a**2 - b2)/b2
        dl = l - lama0
        t = tan(f)
        n2 = ep2 * cos(f)**2
        N = self.a/np.sqrt(1-self.ecc2*(np.sin(f))**2)
        sigm = self.sigma(f)
        xgk = sigm + (dl**2/2) * N * sin(f)*cos(f)*(1 + (dl**2/12)*cos(f)**2*(5-t**2+9*n2+4*n2**2)+ ((dl**4)/360)*cos(f)**4*(61 - 58*t**2 + t**4 + 270*n2 - 330*n2*t**2))
        ygk = dl*N*cos(f)*(1+(dl**2/6)*cos(f)**2*(1 - t**2 + n2) + (dl**4/120)*cos(f)**4*(5 - 18*t**2 + t**4 + 14*n2 - 58*n2*t**2))
        x2000 = xgk * m0
        y2000 = ygk * m0 + strefa * 1000000 + 500000
        return x2000,y2000
    
    
     def XYZ2neu(dX,f,l):
            R = np.array([[-sin(f) * cos(l), -sin(l), cos(f) * cos(l)],
                          [-sin(f) * sin(l), cos(l), cos(f) * sin(l)],
                          [cos(f), 0, sin(f)]])
            return(R.T @ dX)
    

