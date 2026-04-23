'''
market engine

implement with pure numpy first before graphing with python
'''
import matplotlib.pyplot as plt
import numpy as np
from defaults import *
from utils import *

class Trend():
    def __init__(self, a, b, c):
        '''
        - direction on market
        - strength on market
        - variations
        '''
        self.a = a

class Market():
    def __init__(self):
        self.mean = 0
        self.std = 0

        self.velocity = 0
        self.acceleration = 0
    
    def forecast(self):
        pass

    def update(self):
        pass

    def gen_points(self):
        pass

