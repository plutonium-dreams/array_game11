import pygame
import numpy as np
from defaults import *

class Viewport():
    def __init__(self):
        self.width, self.height = scrx/2,scry/2
        self.surface = pygame.Surface((self.width, self.height))
        
        self.ratio = (self.width/scrx, self.height/scry)

    def render():
        pass
    
    def update():
        pass

    def draw(self, points):
        pygame.draw.rect(self.surface, 'green', pygame.Rect((0,0),(100,100)))
        
        
