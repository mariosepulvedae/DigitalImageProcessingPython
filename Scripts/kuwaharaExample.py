#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:41:10 2025

@author: eduardo
"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from kuwaharaFilt import kuwahara

A=cv.imread("nano.tif")[:,:,::-1]
A=cv.cvtColor(A,cv.COLOR_RGB2GRAY)
A=np.asarray(A)
A=np.pad(A,[(4,4),(4,4)],mode="constant")
plt.imshow(A,cmap="gray")
plt.show()
A=A.astype(np.float64)
x,y=A.shape
print(x,y)
i=4
j=4
while i<x-4:
    while j<y-4:
        wind=A[i-4:i+5,j-4:j+5]
        A[i,j]=kuwahara(wind)
        j=j+1
    j=4
    i=i+1
    
A=np.uint8(A[4:x-5,4:y-5])
plt.imshow(A,cmap="gray")
plt.show