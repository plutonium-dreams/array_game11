'''
order book theory

IGNORE THIS FILE
'''
import random, time
import numpy as np
import matplotlib.pyplot as plt

time_horizon = 100
delta_t = 1
# mu = 0.05 / 100 # drift (5% annual return)
sigma = 0.01 # volatility
initial_price = 100

for i in range(100):
    x = np.linspace(0, time_horizon, time_horizon)
    y = np.zeros(time_horizon)
    y[0] = initial_price
    mu = 0.05 / len(y)

    for i in range(1, time_horizon):
        y[i] = y[i-1] * np.exp((mu - 0.5 * sigma ** 2) * delta_t + sigma * np.sqrt(delta_t) * np.random.normal(0,1))

    plt.plot(x,y)

    

plt.show()
