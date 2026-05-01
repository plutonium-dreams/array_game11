'''
Utilities Module
Description: For handling the back-end functions and utilities
'''
from pygame.font import Font

import pygame, os
from defaults import *

pygame.init()


text_main: Font = pygame.font.Font(filename=os.path.join('assets','fonts','vt323-latin-400-normal.ttf'), size=42)
text_viewui = pygame.font.Font(os.path.join('assets','fonts','vt323-latin-400-normal.ttf'), size=24)
text_button: Font = pygame.font.Font(filename=os.path.join('assets','fonts','vt323-latin-400-normal.ttf'), size=32)

def draw_text(list_text):
    '''
    list_text is a list or tuple of strings
    '''
    for text in list_text:
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
        pygame.draw.rect(self.surface, self.color, self.rect, width=5)
        self.surface.blit(self.text, ((self.surface.width-self.text.width)/2,(self.surface.height-self.text.height)/2))

        surf.blit(self.surface, self.centered_pos)

    def update(self):
        # print(pygame.mouse.get_pos())
        if self.surface.get_rect(center=(self.pos)).collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_just_pressed()[0]:
            self.color = colors['button_pressed']
            self.state = True
        else:
            self.color = colors['button']
            self.state = False
            