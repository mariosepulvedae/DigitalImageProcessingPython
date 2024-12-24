# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 03:02:30 2024

@author: Mario Eduardo Sepúlveda Hernández

In this script i've implemented a morphological operation
on a binary image 
It's based on 'majority' operation from MathWorks (2024)
The script analyses 3x3 neighborhood; if there are 5 or more
pixels equal to 1 around the central pixel; it changes its value 
to 1; otherwise, the central pixel will be 0 

n is the number of times the algorithm will be applied on the image
I recommend 10 times (n=10)
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

A=cv.imread("corte.bmp")
A=cv.cvtColor(A,cv.COLOR_BGR2GRAY)
A=np.asarray(A)

plt.subplot(1,3,1)
plt.imshow(A,cmap="gray")
plt.title(label="Original image")
plt.xlabel(xlabel="pixels")
plt.ylabel(ylabel="pixels")

val,B=cv.threshold(A,0,1,cv.THRESH_BINARY+cv.THRESH_OTSU)

plt.subplot(1,3,2)
plt.imshow(B,cmap="gray")
plt.title(label="Binary image")
plt.xlabel(xlabel="pixels")
plt.ylabel(ylabel="pixels")

n=0 
while n<8:
    i=1
    j=0
    while i<(B.shape[0]-1):
        while j<(B.shape[1]-2):
            p=[[B[i-1,j],B[i-1,j+1],B[i-1,j+2]],[B[i,j],B[i,j+1],B[i,j+2]],[B[i+1,j],B[i+1,j+1],B[i+1,j+2]]]
            p=np.asarray(p)
            if np.sum(p)>=5:
                B[i,j+1]=1
            else:
                B[i,j+1]=0
            j=j+1
        j=0
        i=i+1
    n=n+1

plt.subplot(1,3,3)
plt.imshow(B,cmap="gray")
plt.title(label="After morph. operation")
plt.xlabel(xlabel="pixels")
plt.ylabel(ylabel="pixels")
plt.tight_layout()
plt.show
