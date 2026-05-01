'''
Market Engine
Description: Handles the market system of the game. Makes use of Geometric Brownian Motion to simulate a stock market base. This base is then modified by random events and player actions (buy/sell, player-controlled events).


NOTES
implement with pure numpy first before graphing with python

potential models:
- trends and seasons
- buyers and sellers
    - buyers set max
    - sellers set min

break down the market into trends and seasons
trend
- cause; end
- direction
- strength
- speed
& variation (added error)

season(al change)
- period
- frequency
- amplitude
& variation (added error)
'''
import random
import matplotlib.pyplot as plt
import numpy as np
from defaults import *
from utils import *

class Trend():
    def __init__(self, direction, strength, speed):
        '''
        - direction on market
        - strength on market
        - variations
        '''
        self.a = 'a'

class Season():
    def __init__(self, period, frequency, amplitude):
        self.period = period


# class Event()


# Geometric Brownian Motion model
''' would a monte carlo model be better? '''
class Market():
    def __init__(self, initial_price):
        # time horizon has to be premade for this to work

        self.point = 0

        self.time_horizon = 252     # 252 trading days in a year
        self.delta_t = 1
        self.initial_price = initial_price / 100       # accounting for amplification
        self.output = np.array([self.initial_price])
        
        self.mu = 0.05 / self.time_horizon      # % annual yield
        self.sigma = 0.01       # % volatility

        self.test = np.array([self.initial_price])
        
    def update(self):
        pass

    def gen_points(self):
        self.point = self.output[-1] * np.exp((self.mu - 0.5 * self.sigma ** 2) * self.delta_t + self.sigma * np.sqrt(self.delta_t) * np.random.normal(0,1))
        self.output = np.append(self.output, self.point)
        return (self.point*100)//1      # *100 amplifies the effect of the market
    
    def graph(self):
        plt.plot(self.output*100)
        plt.show()


# np.random.seed(1)
# for j in range(100):
#     market = Market(10)
#     for i in range(252):
#         market.gen_points()
#     market.graph()

# plt.show()







