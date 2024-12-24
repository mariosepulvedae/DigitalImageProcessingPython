# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:00:09 2024

@author: Mario Eduardo Sepúlveda Hernández
"""

#With this script you can expand the histogram of an image to obtain
#better contrast

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

R=cv.imread("magrisuave.jpg")
R=np.asarray(R)
histo=cv.calcHist([R], [0], None, [256], [0,256])
levels=np.asarray(histo)
limits = np.nonzero(levels)
r1=min(limits[0])
r2=max(limits[0])
S=(255/(r2-r1))*(R-r1)
S=np.asarray(S).astype(np.int32)

plt.subplot(1,2,1)
plt.imshow(R,cmap="gray")
plt.title(label="Original image")
plt.xlabel(xlabel="pixels")
plt.ylabel(ylabel="pixels")

plt.subplot(1,2,2)
plt.imshow(S,cmap="gray")
plt.title(label="New image (expansion)")
plt.xlabel(xlabel="pixels")
plt.suptitle(t="Histogram expansion")
plt.tight_layout()
plt.show
