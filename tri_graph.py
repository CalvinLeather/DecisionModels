# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 08:22:10 2015

@author: Calvin
"""
import numpy as np
import math

def tri_plot(accumulation, threshold):
    def apply_thresh(x): #applies a threshold to accumulation values
        if x<threshold and x>-threshold:
            return x
        elif x>threshold:
            return threshold
        elif x<-threshold:
            return -threshold
        else:
            raise(ValueError('apply thresh did not get a compatible value'))
    v_thresh = np.vectorize(apply_thresh, otypes = [np.float])
    
    new_acc = v_thresh(accumulation) # between threshold and -threshold
    
    test_array = np.asarray([[.5,0,0,.5],[0,.5,0,.5],[0,0,.5,0]])
    new_acc = test_array
    
    theta = np.radians(60)
    x = new_acc[0] + np.sin(theta)*new_acc[1] + math.cos(theta)*new_acc[2]
    y = math.cos(theta)*new_acc[1] + math.sin(theta)*new_acc[2]
    
    accumulation[0] + (np.sqrt(3)/2)*accumulation[1] + accumulation[2]    

    
    
    
    
    return 1