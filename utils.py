'''
Utilities Module
Description: For handling the back-end functions and utilities
'''
import pygame, os
from defaults import *

pygame.init()
text_main = pygame.font.Font(os.path.join('assets','fonts','vt323-latin-400-normal.ttf'), size=42)
text_viewui = pygame.font.Font(os.path.join('assets','fonts','vt323-latin-400-normal.ttf'), size=24)