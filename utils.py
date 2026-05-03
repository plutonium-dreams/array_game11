'''
Utilities Module
Description: For handling the back-end functions and utilities
'''
from pygame.font import Font

import pygame, os
import numpy as np

from defaults import *

pygame.init()


text_main: Font = pygame.font.Font(filename=os.path.join('assets','fonts','vt323-latin-400-normal.ttf'), size=42)
text_viewui = pygame.font.Font(os.path.join('assets','fonts','vt323-latin-400-normal.ttf'), size=24)
text_button: Font = pygame.font.Font(filename=os.path.join('assets','fonts','vt323-latin-400-normal.ttf'), size=32)
text_dash: Font = pygame.font.Font(filename=os.path.join('assets','fonts','vt323-latin-400-normal.ttf'), size=32)

''' debugging features '''
def debug_menu(state, window, viewport, market):
    if state:
        window.blit(text_viewui.render(f'Zoom: x{(viewport.view_height-100)/1000}',False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+50))

        window.blit(text_viewui.render(f'Number of points:{viewport.view_length}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1))

        window.blit(text_viewui.render(f'GBM Model Values', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+125))
        
        window.blit(text_viewui.render(f'Ann. Yield (mu): {market.mu*market.time_horizon}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+150))
        window.blit(text_viewui.render(f'Vol.(sigma): {market.sigma}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+175))

        # window.blit(text_viewui.render(f'Buy: {bet}' if bet>=0 else f'Sell: {-bet}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+225))

        # window.blit(text_viewui.render(f'Bank: ${money}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+250))
        
        # window.blit(text_viewui.render(f'Shares: ${shares}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+275))
    else:
        pass

def show_boundaries(state, window, viewport):
    if state:
        # center
        pygame.draw.circle(window, 'cyan', (scrx/2,scry/2), outline_width)
        
        # margins
        pygame.draw.line(window, 'cyan', (screen_margin, 0), (screen_margin,scry))
        pygame.draw.line(window, 'cyan', (scrx-screen_margin, 0), (scrx-screen_margin,scry))
        pygame.draw.line(window, 'cyan', (0, screen_margin), (scrx, screen_margin))
        pygame.draw.line(window, 'cyan', (0, scry-screen_margin), (scrx, scry-screen_margin))

        # botton partition
        pygame.draw.line(window, 'fuchsia', (50, viewport.pos[1]+viewport.height+35), (viewport.surface.width+viewport.pos[0]+100,viewport.pos[1]+viewport.height+35))
        # right partition
        pygame.draw.line(window, 'fuchsia', (viewport.surface.width+viewport.pos[0]+100,scry/20+15), (viewport.surface.width+viewport.pos[0]+100,scry-50))
        # bottom right partition
        pygame.draw.line(window, 'fuchsia', (viewport.surface.width+viewport.pos[0]+100,305), (scrx-50,305))

    else:
        pass

class Button():
    def __init__(self, pos, size, text, mode):
        self.surface = pygame.Surface(size)
        self.pos = pos
        self.centered_pos = (pos[0]-self.surface.width/2, pos[1]-self.surface.height/2)  # pos is a 2-item list
        self.rect = pygame.Rect((0,0), (self.surface.width, self.surface.height))
        self.text = text_button.render(text, False, colors['text'])
        self.state = False
        self.color = colors['button']
        self.mode = mode    # either hold or click
        
    def render(self, surf):
        self.surface.fill(colors['bg'])
        pygame.draw.rect(self.surface, self.color, self.rect, width=outline_width)
        self.surface.blit(self.text, ((self.surface.width-self.text.width)/2,(self.surface.height-self.text.height)/2))

        surf.blit(self.surface, self.centered_pos)

    def update(self):
        if self.mode == 'click':
            if self.surface.get_rect(center=(self.pos)).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                self.color = colors['button_pressed']
                self.state = True
            else:
                self.color = colors['button']
                self.state = False
        elif self.mode == 'hold':
            if self.surface.get_rect(center=(self.pos)).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
                self.color = colors['button_pressed']
                self.state = True            
            if pygame.mouse.get_just_released()[0]:
                self.color = colors['button']
                self.state = False

class TextBox():
    def __init__(self, pos, size):
        self.pos = np.array(pos)
        self.surface = pygame.Surface(size)
        self.buttons = []
        # self.rect = pygame.Rect(pos,size)
        

    def render(self,window):
        self.surface.fill(colors['bg_light'])
        window.blit(self.surface, self.pos)
        
        for button in self.buttons:
            button.render(window)
        
        

    def update(self):
        for button in self.buttons:
            button.update()
        pass



class NewsBox(TextBox):
    def __init__(self, pos, size):
        TextBox.__init__(self, pos, size)
        
        # button initialize
        self.button_more = Button(self.pos+np.array([50,25]), (100,50), 'More', 'click')

        self.buttons.extend([self.button_more])
