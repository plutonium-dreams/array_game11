import pygame
import numpy as np
import random
from defaults import *
from utils import *
from market import *

class Viewport():
    def __init__(self):
        self.width, self.height = scrx/2,scry/2
        self.pos=((scrx-self.width)/2,scrx*0.1)
        self.surface = pygame.Surface((self.width, self.height))
        
        self.ciel = 10**5
        self.max_val = self.ciel/100
        self.max_points = 51
        self.view_length = 5

        self.zoom = self.height/self.max_val
        self.interval = 0
        self.total_points = 0
        

        self.y_vals = np.array([0 for i in range(self.max_points)])
        self.filter_y_vals = self.y_vals.copy()
        self.x_vals = np.linspace(0, int(self.width), len(self.y_vals))

        

    def convert_point(self, point):
        return self.height/2 - ((point-self.y_vals[-1]) * self.zoom)
    
    def render(self, surface):
        surface.blit(self.surface, self.pos)

        # render the y marker points
        y_marker_surface = pygame.Surface((100,scry/2+50))
        for i in range(-2*self.ciel, 2*self.ciel, int(self.ciel/10)):
            mark = text_viewui.render(f'{i}', False, colors['ui'])
            y_marker_surface.blit(mark, (75-mark.size[0],self.convert_point(i)-mark.size[1]/2+25))
        surface.blit(y_marker_surface, (self.pos[0]-100, self.pos[1]-25))

        # render the x marker points
        ''' optimize this josef '''
        x_marker_surface = pygame.Surface((scrx/2+50, 50))
        for i in range(len(self.x_vals)):
            mark = text_viewui.render(f'{self.total_points-i}', False, colors['ui'])
            if (10 < self.view_length <= 25) & (i%(2* len(str(self.view_length)))!=0) or (25 < self.view_length <= 52) & (i%(5* len(str(self.view_length)))!=0):
                continue

            # Will optimize more in the future

            # if 10 < self.view_length <= 25 & i%(2* len(str(self.view_length)))!=0:
            #     continue
            # elif 25 < self.view_length <= 52 & i%(5* len(str(self.view_length)))!=0:
            #     continue

            else:
                x_marker_surface.blit(mark, (self.x_vals[-i-1]-mark.size[0]/2+25,10))
        surface.blit(x_marker_surface, (self.pos[0]-25,self.pos[1]+self.height))

    
    def update(self, num=None):
        self.surface.fill(colors['bg'])
        self.total_points +=1
        # the specific code that adds a new y value in the data set
        self.y_vals = np.append(self.y_vals, random.randrange(-self.ciel, int(self.ciel/10), int(self.ciel/1000)))
        # self.y_vals = np.append(self.y_vals, num)
      
        # maxes out the number of points to draw 
        # if len(self.y_vals) >= self.max_amt:
        #     self.y_vals = self.y_vals[:-(self.max_amt+1):-1][::-1]
        if len(self.y_vals) >= self.max_points:
            self.y_vals = self.y_vals[:-(self.max_points+1):-1][::-1]        


    def draw(self, y_vals):
        ''' 
        y_vals must be of ndarray format
        '''
        self.filter_y_vals = np.append(self.y_vals[:-(self.view_length+1):-1][::-1], y_vals)
        self.x_vals = np.linspace(0, int(self.width), len(self.filter_y_vals))
        
        points = np.column_stack((self.x_vals, self.convert_point(self.filter_y_vals)))
        
        pygame.draw.lines(self.surface, colors['main'], False, points, width=3)

        # print(self.y_vals)
    
    def scale_y(self, zom):

        # Occam's Razor 😮

        # self.surface.fill(colors['bg'])        
        # if (self.max_val >= 0) and (self.max_val <= self.ciel):
        #     self.max_val += (zom * self.ciel/100)
        #     self.zoom = self.height/self.max_val
        #     print(1)
        # elif self.max_val < 0 :
        #     self.max_val = self.ciel/100
        #     print(2)
        # elif self.max_val > self.ciel:
        #     self.max_val = self.ciel - self.ciel/100
        #     print(3)
        self.surface.fill(colors['bg'])        
        self.max_val += (zom * self.ciel/100)
        self.zoom = self.height/self.max_val

    def scale_x(self, zom):
        self.surface.fill(colors['bg'])
        self.view_length += zom

        # Incorporated lapaw error catching conditionals into keybind conditionals instead

        # if 5 < self.view_length < self.max_points:
        #     self.view_length += zom
        # elif self.view_length == 5 and zom > 0:
        #     self.view_length += zom
        # elif self.view_length == 51 and zom < 0:
        #     self.view_length -= 1