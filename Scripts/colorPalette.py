#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:30:52 2024

@author: Mario Eduardo Sepúlveda Hernández

This script is based on Chopra, Y. (2020). Image Segmentation using 
Sklearn and K-Means
https://github.com/Yuvrajchopra25/Project-8-Image-Segmentation-using-
Sklearn-and-K-Means

To obtain the colors
You can use it 
"""

import cv2 as cv
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np 


A=cv.imread("sonoshee.jpeg")
A=cv.cvtColor(A,cv.COLOR_BGR2RGB)
B=A.reshape((-1,3))
B=np.float32(B)

criteria=(cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100,0.9)
k=8 #Clusters
comp, labels, centers = cv.kmeans(B, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
result = centers[labels.flatten()]
result = result.reshape((A.shape))

colors=[]
j=0
pC=[]

while j<k:
    colors.append(centers[j])
    a = np.zeros((50,50,3),dtype='uint8')
    # Color Swatch
    a[:,:,:] = colors[j]
    pC.append(a)
    j=j+1

fig = plt.figure(layout="constrained",figsize=(8, 4))
gs = GridSpec(2, k, figure=fig)
ax0 = fig.add_subplot(gs[0,:])
#fig.subplots_adjust(hspace=0,bottom=0,left=0)
ax0.imshow(result)
ax0.axis("off")
n=0
while n<k:
    ax1 = fig.add_subplot(gs[-1:,n]) 
    ax1.imshow(pC[n])
    ax1.axis("off")
    #fig.subplots_adjust(hspace=0,bottom=0.2,left=0,wspace=0.1)
    n=n+1
plt.suptitle(t="Redline (2009). Dir. Takeshi Koike ")
plt.show
plt.savefig("sonosheeSeg.jpg",dpi=500)
print(colors)