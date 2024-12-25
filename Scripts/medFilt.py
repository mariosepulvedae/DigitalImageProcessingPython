#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:19:20 2024

@author: Mario Eduardo Sepúlveda Hernández

This function receives a Grayscale image; before use it be sure
your image innot in RGB layers but grayscale
"""
import numpy as np

def medianFilt(A):
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
    return A
    
    
    
    