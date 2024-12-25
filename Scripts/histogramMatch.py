# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 02:17:26 2024

@author: Mario Eduardo Sepúlveda Hernández

With this script you can apply the histogram match
You will obtain a histogram with the shape you desire, from a 
reference image
"""

from skimage.exposure import match_histograms
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


def histExp(R):
    histo=cv.calcHist([R], [0], None, [256], [0,256])
    levels=np.asarray(histo)
    limits = np.nonzero(levels)
    r1=min(limits[0])
    r2=max(limits[0])
    S=(255/(r2-r1))*(R-r1)
    S=np.asarray(S).astype(np.int32)
    return S


reference=cv.imread("chest_x_ray.jpg")[:,:,::-1]
reference=np.asarray(reference)
plt.subplot(2,3,1)
plt.imshow(reference,cmap="gray")
plt.title(label="Reference Image")
plt.xlabel(xlabel="pixels")
plt.ylabel("pixels")
plt.yticks(rotation = 90)
plt.yticks(rotation = 90)
plt.subplot(2,3,4)
plt.hist(reference.ravel(),256,[0,256],color="#f85300")
plt.title("Reference histogram")
plt.xlabel(xlabel="Intensity levels")
plt.ylabel(ylabel="N(r)")
plt.yticks(rotation = 90)
plt.ticklabel_format(axis='y', style='sci', scilimits=(4,4))


R=cv.imread("cancer_pulmon.jpg")[:,:,::-1]
R=np.asarray(R)
plt.subplot(2,3,2)
plt.imshow(R,cmap="gray")
plt.title(label="Image R")
plt.xlabel(xlabel="pixels")
plt.ylabel("pixels")
plt.ticklabel_format(axis='y', style='sci', scilimits=(4,4))
plt.yticks(rotation = 90)
plt.subplot(2,3,5)
plt.hist(R.ravel(),256,[0,256],color="#ab2e76")
plt.title("Histogram")
plt.xlabel(xlabel="Intensity levels")
plt.ylabel(ylabel="N(r)")
plt.yticks(rotation = 90)
plt.ticklabel_format(axis='y', style='sci', scilimits=(4,4))
S=histExp(R)

matched = match_histograms(S, reference,channel_axis=2)
plt.subplot(2,3,3)
plt.imshow(matched,cmap="gray")
plt.title(label="New image S")
plt.xlabel(xlabel="pixels")
plt.ylabel("pixels")
plt.ticklabel_format(axis='y', style='sci', scilimits=(4,4))
plt.yticks(rotation = 90)
plt.subplot(2,3,6)
plt.hist(matched.ravel(),256,[0,256],color="#08c477",linewidth=3)
plt.title("New histogram")
plt.xlabel(xlabel="Intensity levels")
plt.ylabel(ylabel="N(r)")
plt.yticks(rotation = 90)
plt.axis([0,255,0,500000])
plt.ticklabel_format(axis='y', style='sci', scilimits=(4,4))
plt.suptitle(t="Histogram Matching")
plt.tight_layout()
plt.show
