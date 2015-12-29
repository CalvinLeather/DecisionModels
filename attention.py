# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:52:49 2015

@author: Calvin
"""
import numpy as np
def create_attn_array(time_points, trans_prob):
    time_points = 10000
    
    #model 1 is attentional multi-attribute
    
    starting_attribute = np.random.choice([1,2])
    
    x = np.random.rand(time_points)
    p_switch_1 = x > trans_prob
    p_switch_2 = x < (1-trans_prob)
    
    attn = np.zeros(time_points)
    attn[0:len(attn)] = starting_attribute
    
    for index in range(time_points): #markov logic to generate attentional array
        if p_switch_1[index]:
            if attn[index] == 2:
                attn[index+1:len(attn)] = 1
        elif p_switch_2[index]:
            if attn[index] == 1:
                attn[index+1:len(attn)] = 2
    return attn