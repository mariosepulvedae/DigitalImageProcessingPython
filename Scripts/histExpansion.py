#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 03:35:29 2024

@author: Mario Eduardo Sepúlveda Hernández

In this file i've implemented the Histogram Expansion as a function
Thus, you can use it multiple times 
To call it, you just need to write 

from histExpansion import histogramExpansion

"""
import cv2 as  cv
import numpy as np
def histogramExpansion(R):
    histo=cv.calcHist([R], [0], None, [256], [0,256])
    levels=np.asarray(histo)
    limits = np.nonzero(levels)
    r1=min(limits[0])
    r2=max(limits[0])
    S=(255/(r2-r1))*(R-r1)
    S=np.asarray(S).astype(np.int32)
    return S