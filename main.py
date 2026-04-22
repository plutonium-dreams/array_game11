'''
Math 154 Final Project
Black Market

To do:
[ ] implement the market system
    [ ] moving graph
    [ ] graph that moves according to principles of the stock market
        [ ] the long-term and short-term factors

'''
import pygame, random, os, sys
import numpy as np 
import sympy as sp
from defaults import *
from graph import *

pygame.init()

window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()
pygame.display.set_caption('BLACK MARKET')

viewport = Viewport()

outline_width = 5


points = [(1,2),(3,4), (-1,3)]




def game():
    while True:
        window.fill('black')
        viewport.surface.fill('black')

        viewport.draw([10])

        

        
        # outline
        pygame.draw.rect(window,'white',pygame.Rect(((scrx-viewport.width)/2-outline_width,scrx*0.1-outline_width),(viewport.width+2*outline_width,viewport.height+2*outline_width)),width=outline_width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    coords.pop()

        window.blit(viewport.surface,((scrx-viewport.width)/2,scrx*0.1))

        pygame.display.update()
        pygame.clock.tick(60)

game()