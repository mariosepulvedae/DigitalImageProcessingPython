#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 23:41:33 2025

@author: Mario Sepúlveda-Hernández

This script will segment an image in 4 clusters with K-means algorithm
but first, we need to enhance the image
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage.exposure import match_histograms
from histExpansion import histogramExpansion
from medFilt import medianFilt


A=cv.imread("x-ray-bones.tif")[:,:,::-1]
A=cv.cvtColor(A,cv.COLOR_RGB2GRAY)
dim=A.shape
A=np.asarray(A)

plt.subplot(2,2,1)
plt.imshow(A,cmap="gray")
plt.title(label="Orignal image")
plt.axis("off")


A=medianFilt(A)
plt.subplot(2,2,2)
plt.imshow(A,cmap="gray")
plt.title(label="Without noise")
plt.axis("off")

reference=cv.imread("chest_x_ray.jpg")[:,:,::-1]
reference=cv.cvtColor(reference,cv.COLOR_RGB2GRAY)
reference=np.asarray(reference)

A=match_histograms(A,reference)
plt.subplot(2,2,3)
plt.imshow(A,cmap="gray")
plt.title(label="Enhanced image")
plt.axis("off")

A=A.reshape(-1)
A=np.float32(A)

n=100
epsilon=0.9
criteria=(cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, n,epsilon)
k=4#Clusters

comp,label,center=cv.kmeans(data=A, K=k, bestLabels=None, criteria=criteria, attempts=10, flags=  cv.KMEANS_RANDOM_CENTERS )
center=np.uint8(center)
result=center[label.flatten()]
result=result.reshape((dim))

result=np.asarray(result)
plt.subplot(2,2,4)
plt.imshow(result,cmap="cool")
plt.axis("off")
plt.title(label="Segmented image")
plt.colorbar()
plt.suptitle(t="K-means")
plt.show
plt.savefig(fname="imageSegmented.jpg",dpi=500)