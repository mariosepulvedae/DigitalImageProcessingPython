# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 16:49:46 2024

@author: Mario Eduardo Sepúlveda Hernández

In this script i implemented the median filter to reduce the 
"Salt & pepper" noise

The script analyses 3x3 neighborhoods and change the value
of the central pixel to the median of the neighborhood 

"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

A=cv.imread("x-ray-bones.tif")
A = cv.cvtColor(A, cv.COLOR_BGR2GRAY)
A=np.asarray(A)

plt.subplot(1,2,1)    
plt.imshow(A,cmap="gray")
plt.title(label="Salt & pepper noise")
plt.xlabel(xlabel="pixels")
plt.ylabel(ylabel="pixels")

i=1
j=0
while i<(A.shape[0]-1):
    while j<(A.shape[1]-2):
        p=[[A[i-1,j],A[i-1,j+1],A[i-1,j+2]],[A[i,j],A[i,j+1],A[i,j+2]],[A[i+1,j],A[i+1,j+1],A[i+1,j+2]]]
        p=np.asarray(p)
        valor=np.median(p)
        A[i,j+1]=valor
        j=j+1
    j=0
    i=i+1

plt.subplot(1,2,2)
plt.imshow(A,cmap="gray")
plt.title(label="Image without noise")
plt.xlabel(xlabel="pixels")
plt.ylabel(ylabel="pixels")
plt.tight_layout()
plt.show
