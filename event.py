'''
Events Engine

Makes the game not boring!
'''

'''
PLAN

- TECHNICALITIES
    - Event engine handles the event selection, event processing
    - events are subclasses from a parent event class
    - keep all the possible events in a numpy array

- EVENTS
    - ATTRIBUTES
        - level: 1,2, or 3
        - conditions for proc
        - change in mu
        - change in sigma
        - change in player balance
    
    
    - LEVEL 1
        - picked-up cash on the ground
        - relative gave money
        - pickpocket
    - LEVEL 2
        - market rumors
    - LEVEL 3
        - war
        - pandemic
        - cuop


'''
import pygame, os
import numpy as np
# import pandas as pd
from defaults import *
from utils import *


class Event():
    def __init__(self, level):
        ''' 
        << Event Documentation here >>>
        Name:
        Description:
        Trigger Condition:
        End Condition:
        '''
        self.LEVEL = level


