import pygame
import numpy as np
import random
from defaults import *
from utils import *

class Viewport():
    def __init__(self):
        self.width, self.height = scrx/2,scry/2
        self.surface = pygame.Surface((self.width, self.height))
        self.max_val = scry

        self.zoom = self.height/self.max_val
        self.interval = 0

        self.y_vals = np.array([0,0,0])

        self.ciel = 10000

    def convert_point(self, point):
        return self.height/2 - ((point-self.y_vals[-1]) * self.zoom)
    
    def render(self, surface):
        surface.blit(self.surface, ((scrx-self.width)/2,scrx*0.1))
    
    def update(self, num = None):
        self.surface.fill(colors['bg'])
        
        # the specific code that adds a new y value in the data set
        self.y_vals = np.append(self.y_vals, random.randrange(0, self.ciel, int(self.ciel/100)))
        # self.y_vals = np.append(self.y_vals, num)
      
        # maxes out the number of points to draw to 10
        n = 10
        if len(self.y_vals) >= n:
            self.y_vals = self.y_vals[:-(n+1):-1][::-1]

    def draw(self, y_vals):
        ''' 
        y_vals must be of ndarray format
        '''
        self.y_vals = np.append(self.y_vals, y_vals)
        x_vals = np.linspace(0, int(self.width), len(self.y_vals))
        
        points = np.column_stack((x_vals, self.convert_point(self.y_vals)))
        
        pygame.draw.lines(self.surface, colors['main'], False, points, width=3)

        # markers; move outside of viewport
        # for i in range(11):
        #     pygame.draw.rect(self.surface, 'blue', pygame.Rect((0,self.height- (self.ciel*(i)/10 * self.ratio)),(10,10)))
        #     self.surface.blit(text_main.render(f'{self.ciel/10*i}',False,'blue'),(10,self.height- (self.ciel*(i)/10 * self.ratio)))
        # text rendering
        
        for i in range(-self.ciel, 2*self.ciel, int(self.ciel/5)):
            mark = text_viewui.render(f'{i}', False, colors['ui'])
            self.surface.blit(mark, (0,self.convert_point(i)-mark.size[1]/2))

        print(self.y_vals)
    
    def scale(self, val):
        self.surface.fill(colors['bg'])        
        if (self.max_val > 0) and (self.max_val < self.ciel):
            self.max_val += (val * self.ciel/100)
            if self.max_val < 0:
                self.max_val = scry
            self.zoom = self.height/self.max_val
        
