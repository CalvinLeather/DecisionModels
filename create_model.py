# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:05:14 2015

@author: Calvin
"""
import numpy as np

def create_model(items, value_dict, alpha, beta, noise_mix, value_amp, time_points, n_reps, threshold):
    history = []
    end_times = []
    all_accumulators = []
    n_colors = len(items[:,0])
    n_shapes = len(items[:,1])
    key = np.reshape([items[:,0],items[:,1]], n_shapes+n_colors)
    
    get_value = np.vectorize(value_dict.get)

    c_values = np.repeat(get_value(items[:,0]),time_points) *alpha
    s_values = np.repeat(get_value(items[:,1]),time_points) *alpha
    c_values = np.reshape(c_values,(n_colors,time_points))
    s_values = np.reshape(s_values,(n_shapes,time_points))
    values = np.vstack((c_values,s_values))
    
    for index in range(n_reps):
        noise = np.random.randn(n_colors+n_shapes,time_points)*beta
        noise_cum = np.cumsum(noise, 1)
        
        values_cum = np.cumsum(values,1) #needs to be in loop because of for x in vals
        
        vals, count = np.unique(items, return_counts=True)
        
        for x in vals[count>1]:
            indices = np.where(key==vals[count>1])[0]
            shared_noise = (noise_mix)*noise_cum[indices[0]]
            noise_cum[indices] =  np.vstack((shared_noise,shared_noise))+ (1-noise_mix)*noise_cum[indices] 
            #np.corrcoef(noise_cum[3], noise_cum[2])
            values_cum[indices] = np.power(value_amp, len(indices))*values_cum[indices]#*len(indices)
            
        accumulators = noise_cum+values_cum
            
        item_accumulator = accumulators[0:n_colors]+accumulators[n_colors:n_colors+n_shapes]
        
        winner = -1
        for x in range(len(item_accumulator[0])):    
            sorted_indx = np.argsort(item_accumulator[:,x])
            max_diff = item_accumulator[sorted_indx[-1],x]-item_accumulator[sorted_indx[-2],x]
            if max_diff>threshold:
                winner = sorted_indx[-1]
                break
        if winner == -1:
            winner = 'timeout'
                
        history.append(winner)
        end_times.append(x)
        
        #item, time = np.where(item_accumulator>10)
        #if time.size == 0:
        #    winner = 'timeout'
        #else:
        #    winner = item[np.argmin(time)]      
        #history.append(winner)
        all_accumulators.append(item_accumulator)
        
    return all_accumulators, history, end_times