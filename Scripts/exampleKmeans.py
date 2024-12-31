#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 02:12:18 2024

@author: Mario Eduardo Sepúlveda Hernández

    Script based on: 
    https://docs.opencv.org/4.x/d1/d5c/tutorial_py_kmeans_opencv.html
    
    cv.TERM_CRITERIA_EPS: stop the algorithm iteration if specified accuracy, 
        epsilon, is reached.
    
    cv.TERM_CRITERIA_MAX_ITER: stop the algorithm after the specified number
        of iterations, max_iter.
    
    cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER - stop the iteration when
        any of the above condition is met.

"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

A=cv.imread("alphaville.jpg")[:,:,::-1]
A=cv.cvtColor(A, cv.COLOR_RGB2GRAY)
plt.subplot(1,2,1)
plt.imshow(A,cmap="gray")
plt.axis("off")
plt.title(label="Original image ")

dim=A.shape
A=A.reshape(-1) # The 2D image is now 1D
A=np.float32(A)

n=100
epsilon=0.9
criteria=(cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, n,epsilon)
k=4 #Clusters

comp,label,center=cv.kmeans(data=A, K=k, bestLabels=None, criteria=criteria, attempts=10, flags=  cv.KMEANS_RANDOM_CENTERS )


center = np.uint8(center)
res = center[label.flatten()]
res = res.reshape((dim))

res=np.asarray(res)

plt.subplot(1,2,2)
plt.title(label="Segmented image k=4 ")
plt.imshow(res,cmap="gray")
plt.axis("off")
plt.suptitle(t="K-means for Grayscale image", y=0.88)
plt.show

plt.savefig("alphavilleKMeans.jpg", dpi=500)