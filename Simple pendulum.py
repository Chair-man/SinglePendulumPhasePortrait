# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 14:25:46 2018

@author: Rishi Acharya
"""

import matplotlib
import math

G = 9.80665
L = 4.358511111111111
MAX_THETA_DOTS = sorted([0.75, 1.5, 2.25, 3, 3.75, 4.5, 5.25])
# MAX_THETA_DOTS Calculated to ensure (pi,0) is a solution (4.428690551)
ANGLE_SENSITIVITY = 0.1 # Domain between samples
MAX_THETA = 9           # Domain upper bound
MIN_THETA = -1*MAX_THETA


def generate_derivative(angle:float,
                        sgn:int,
                        max_theta_dot:float,
                        g:float,
                        l:float)->float:
    try:
        derivative =\
            sgn * math.sqrt((max_theta_dot**2)-\
                        (2*g/l)*(1-math.cos(angle)))
    except ValueError:  # SQRT(negative)-> derivative doesn't exist
        return 0
    return derivative

theta = MIN_THETA
x_set, y_set_pos, y_set_neg = [], [], []
for max_theta_dot in MAX_THETA_DOTS:
    x_set.append([])
    y_set_pos.append([])
    y_set_neg.append([])
    theta = MIN_THETA
    while theta <= MAX_THETA:
        x_set[MAX_THETA_DOTS.index(max_theta_dot)].append(theta)
        y_set_pos[MAX_THETA_DOTS.index(max_theta_dot)].append(
                generate_derivative(theta, 1, max_theta_dot, G, L)
                )
        y_set_neg[MAX_THETA_DOTS.index(max_theta_dot)].append(
                generate_derivative(theta, -1, max_theta_dot, G, L)
                )
        theta += ANGLE_SENSITIVITY

colors = ['tab:red', 'tab:orange', 'y',
          'tab:green', 'tab:cyan', 'tab:blue', 'tab:purple']
fig = matplotlib.pyplot.figure()
axes = fig.add_subplot(111)
for i in range(len(MAX_THETA_DOTS)):
    axes.plot(x_set[i], y_set_pos[i],
                           c=colors[i-((i//len(colors))*len(colors))],
                           )    # Loops circular through colors
    axes.plot(x_set[i], y_set_neg[i],
                           c=colors[i-((i//len(colors))*len(colors))],
                           )
axes.grid()
axes.set(
        xlabel='Theta', ylabel='Theta dot', title='Phase portrait'
        )
matplotlib.pyplot.savefig('pendulum phase portrait.jpg')