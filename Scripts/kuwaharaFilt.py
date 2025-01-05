#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:04:59 2025

@author: Mario Eduardo Sepúlveda Hernández

In this script i've implemented a version of Kuwahara Filter
This version is slow

For better results, you can use the version 
Copyright (c) 2007, Luca Balbi
All rights reserved.

and  Andrew Dussault, (2015 ): https://github.com/adussault/python-kuwahara
"""

import numpy as np
import statistics as st


def kuwahara(wind):
    m,n=wind.shape
    center=int(m/2)+1
    v1=wind[0:center,0:center]
    v2=wind[0:center,center-1:n]
    v3=wind[center-1:m,0:center]
    v4=wind[center-1:m,center-1:n]
    vec=[v1.flatten(),v2.flatten(),v3.flatten(),v4.flatten()]
    
    means=[]
    variances=[]
    
    for data in vec:
        means.append(st.mean(data))
        variances.append(st.variance(data))

    
    variances=np.asarray(variances)
    means=np.asarray(means)

    env=np.where(variances == variances.min())
    return means[env[0][0]]
