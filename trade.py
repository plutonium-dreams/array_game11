'''
trading engine
'''
import pygame, os
import numpy as np
from defaults import *
from utils import *

class Trade():
    def __init__(self):
        self.button_buy = Button((3*scrx/8,7*scry/8), (100,50), 'Buy', 'hold')
        self.button_sell = Button((5*scrx/8,7*scry/8), (100,50), 'Sell', 'click')

    def render(self, window):
        self.button_buy.render(window)
        self.button_sell.render(window)

    def update(self):
        self.button_buy.update()
        self.button_sell.update()

