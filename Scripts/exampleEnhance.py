# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:05:24 2024

@author: Mario Eduardo Sepúlveda Hernández

In this script i will use the median filter, the histogram expansion, and the 
histogram matching to enhance an image and make easier the analysis

"""

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 
from histExpansion import histogramExpansion
from medFilt import medianFilt
from skimage.exposure import match_histograms

R=cv.imread("corte-cerebro.jpg")[:,:,::-1]
R=cv.cvtColor(R,cv.COLOR_RGB2GRAY)
R=np.asarray(R)

plt.subplot(1,3,1)
plt.imshow(R,cmap="gray")
plt.title(label="Original image")
plt.ylabel(ylabel="pixels")
plt.xlabel(xlabel="pixels")

S=medianFilt(R)
S=histogramExpansion(S)
plt.subplot(1,3,2)
plt.imshow(S,cmap="gray")
plt.title(label="Image without noise")
plt.ylabel(ylabel="pixels")
plt.xlabel(xlabel="pixels")

reference=cv.imread("chest_x_ray.jpg")[:,:,::-1]
reference=cv.cvtColor(reference,cv.COLOR_RGB2GRAY)
reference=np.asarray(reference)

result=match_histograms(S,reference)
plt.subplot(1,3,3)
plt.imshow(result,cmap="gray")
plt.ylabel(ylabel="pixels")
plt.xlabel(xlabel="pixels")
plt.title(label="Image enhanced")
plt.tight_layout()
plt.show
