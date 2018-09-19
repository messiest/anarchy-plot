#!/usr/bin/env python3

import os
import sys
import warnings

import numpy as np
from matplotlib import pyplot as plt


warnings.filterwarnings('ignore')

if sys.platform == 'win32':
    DESKTOP = os.path.join(os.environ['USERPROFILE'], 'Desktop')  # Windows
else:
    DESKTOP = os.path.join(os.path.expanduser('~'), 'Desktop')  # Unix


def anarchy_plot():
    def f(x):
        return 2 + np.sqrt(-1 * (x-2)**2 + 1)

    def g(x):
        return 2 - np.sqrt(-1 * (x-2)**2 + 1)

    def h(x):
        return 3 * x - 3

    def i(x):
        return -3 * x + 9

    def j(x):
        return 0.2 * x + 1.7

    x = np.linspace(0, 5, 10000)

    for fn in [f, g, h, i, j]:
        plt.plot(x, fn(x), color='r')

    plt.ylim(0, 4)
    plt.xlim(0, 4)
    plt.axis('off')

    plt.savefig(os.path.join(DESKTOP, 'ANARCHY!!!.png'))


if __name__ == "__main__":
    anarchy_plot()
