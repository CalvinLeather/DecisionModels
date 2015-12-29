# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 10:53:08 2015
Uses luce choice rule to approximate the probability of looking at item x at each time point
@author: Calvin
"""
import numpy as np

def luce_sim(item_accumulator):
    item_accumulator[item_accumulator<0]=0
    total = np.sum(item_accumulator,0)
    p_look = np.divide(item_accumulator, total)
    return p_look