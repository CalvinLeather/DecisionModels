# -*- coding: utf-8 -*-
"""
Spyder Editor

Main body of the program, defines variables, creates and displays models
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from display import get_name, plot3, hist_plot
from create_model import create_model
from luce_sim import luce_sim

time_points = 1000
n_reps = 10000
threshold = 5
alpha = .01 #scaling on value
beta = .2 #scaling on noise
noise_mix = .5 #0-1 indicating how much shared noise is correlated
value_amp = 1. #multiplication factor >1 for shared value
history = []

sns.set(rc={"figure.figsize": (5,12)})
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.set_palette(flatui)

items = np.asarray([['green', 'square'], ['red', 'circle'], ['red', 'triangle']])
value_dict = {'green': 5, 'red': 3, 'square': 5, 'circle':7, 'triangle':2}
names = [get_name(items, x) for x in range(items.shape[0])]
n_items = len(items)

all_accumulators, history, end_times = create_model(items, value_dict, alpha, beta, noise_mix, value_amp, time_points, n_reps, threshold)
item_accumulator = all_accumulators[0]
winner = history[0]

p_look = np.zeros(all_accumulators[0].shape)
for x in range(len(all_accumulators)):
    p_look += luce_sim(all_accumulators[x])
    
p_look= p_look/x

if 1:
    plot3(items, names, winner, item_accumulator, history, p_look)
if 0:
    hist_plot(end_times, history, items)
