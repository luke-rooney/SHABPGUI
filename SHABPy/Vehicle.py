#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:51:02 2022

@author: lukerooney
"""
import numpy
from stl import mesh
from . MethodsModule import *
from . FlightDynamics import *

class Vehicle():
    def __init__(self, M, gamma, cbar, span, sref, xref, yref, zref, m, stlfile, compression, expansion, Ixx, Iyy, Izz, Ixz):
        self.M     = M
        self.gamma = gamma
        self.cbar  = cbar
        self.span  = span
        self.sref  = sref
        self.yref  = yref
        self.xref  = xref
        self.zref  = zref
        self.m     = m
        self.mesh  = mesh.Mesh.from_file(stlfile)
        self.C     = getInertiaCoeffs(Ixx, Iyy, Izz, Ixz)

        if compression == 1:
            self.compression = NewtonianMethod(M, gamma)
        elif compression == 2:
            self.compression = NewtonianPrandtlMeyer(M, gamma)
        elif compression == 3:
            self.compression = ModifiedNewtonian(M, gamma)
        elif compression == 4:
            self.compression = HankeyFlatSurface(M, gamma)
        elif compression == 5:
            self.compression = VanDykeUnified(M, gamma)
        elif compression == 6:
            self.compression = BusemannSecondOrderTheory(M, gamma)
        else:
            self.compression = NewtonianMethod(M, gamma)

        if expansion == 1:
            self.expansion = NewtonianMethod(M, gamma)
        elif expansion == 2:
            self.expansion = NewtonianPrandtlMeyer(M, gamma)
        elif expansion == 3:
            self.expansion = ModifiedNewtonian(M, gamma)
        elif expansion == 4:
            self.expansion = HankeyFlatSurface(M, gamma)
        elif expansion == 5:
            self.expansion = VanDykeUnified(M, gamma)
        elif expansion == 6:
            self.expansion = BusemannSecondOrderTheory(M, gamma)
        else:
            self.expansion = NewtonianMethod(M, gamma)

    def UpdatePanelMethod(self, method):
        if method == 1:
            self.compression = NewtonianMethod(self.M, self.gamma)
            self.expansion   = NewtonianMethod(self.M, self.gamma)
        elif method == 2:
            self.compression = NewtonianPrandtlMeyer(self.M, self.gamma)
            self.expansion   = NewtonianPrandtlMeyer(self.M, self.gamma)
        elif method == 3:
            self.compression = ModifiedNewtonian(self.M, self.gamma)
            self.expansion   = ModifiedNewtonian(self.M, self.gamma)
        elif method == 4:
            self.compression = HankeyFlatSurface(self.M, self.gamma)
            self.expansion   = HankeyFlatSurface(self.M, self.gamma)
        elif method == 5:
            self.compression = VanDykeUnified(self.M, self.gamma)
            self.expansion   = VanDykeUnified(self.M, self.gamma)
        elif method == 6:
            self.compression = BusemannSecondOrderTheory(self.M, self.gamma)
            self.expansion   = BusemannSecondOrderTheory(self.M, self.gamma)
        else:
            self.compression = NewtonianMethod(self.M, self.gamma)
            self.expansion   = NewtonianMethod(self.M, self.gamma)

    def UpdateCompression(self, method):
        if method == 1:
            self.compression = NewtonianMethod(self.M, self.gamma)
        elif method == 2:
            self.compression = NewtonianPrandtlMeyer(self.M, self.gamma)
        elif method == 3:
            self.compression = ModifiedNewtonian(self.M, self.gamma)
        elif method == 4:
            self.compression = HankeyFlatSurface(self.M, self.gamma)
        elif method == 5:
            self.compression = VanDykeUnified(self.M, self.gamma)
        elif method == 6:
            self.compression = BusemannSecondOrderTheory(self.M, self.gamma)
        else:
            self.compression = NewtonianMethod(self.M, self.gamma)

    def UpdateExpansion(self, method):
        if method == 1:
            self.expansion   = NewtonianMethod(self.M, self.gamma)
        elif method == 2:
            self.expansion   = NewtonianPrandtlMeyer(self.M, self.gamma)
        elif method == 3:
            self.expansion   = ModifiedNewtonian(self.M, self.gamma)
        elif method == 4:
            self.expansion   = HankeyFlatSurface(self.M, self.gamma)
        elif method == 5:
            self.expansion   = VanDykeUnified(self.M, self.gamma)
        elif method == 6:
            self.expansion   = BusemannSecondOrderTheory(self.M, self.gamma)
        else:
            self.expansion   = NewtonianMethod(self.M, self.gamma)
