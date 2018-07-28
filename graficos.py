#! /usr/bin/python
# -*- coding: iso-8859-15 -*-
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)
x = linspace(0, 5, 10)
y = x ** 2
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('titulo')
show()