# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:13:50 2020

@author: Riddhi
"""

import numpy as np
import matplotlib.pyplot as plt


# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()