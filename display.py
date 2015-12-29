# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:15:16 2015

@author: Calvin
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def get_name(items, winner):
    return items[winner][0] + ' ' + items[winner][1]
    
def plot3(items, names, winner, item_accumulator, history, p_look):
    n_items = len(items)
    plt.figure(figsize=(10,20))
    ax = plt.subplot(311)
    for i in range(n_items):
        ax.plot(item_accumulator[i], label= get_name(items, i))
        plt.title('Race model simulation of 3AFC. Winner = ' +  get_name(items, winner))
        plt.legend()
        
    freq, bins = np.histogram(history, bins = range(n_items+1))    
    bx = plt.subplot(312)
    bx.bar([1,2,3],freq, width=.4)
    bx.set_xticks([1,2,3])
    bx.set_xticklabels(names, horizontalalignment = 'left')
    
    cx = plt.subplot(313)
    cx.set_ylim([0,1])
    for i in range(n_items):
        cx.plot(p_look[i], label= get_name(items, i))
        plt.title('Luce model of p(look). Winner = ' +  get_name(items, winner))
        plt.legend()
    return 1