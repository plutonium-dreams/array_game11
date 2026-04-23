'''
Math 154 Final Project
Black Market

To do:
[ ] implement the market system
    [/] moving graph
    [ ] add viewport utilities
        [ ] zoom and shi
    [ ] graph that moves according to principles of the stock market
        [ ] the long-term and short-term factors
[ ] implement events into the game
    [ ] random events:
        [ ] war
        [ ] pandemic
        [ ] coup
        [ ] technology

1 = 1 million

'''
import pygame, random, os, sys
import numpy as np 
import sympy as sp
from defaults import *
from utils import *
from graph import *

pygame.init()

window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()
pygame.display.set_caption('BLACK MARKET')

viewport = Viewport()




def game():
    thing  = 0
    while True:
        window.fill(colors['bg'])
        
        viewport.render(window)
        viewport.draw([])

        # if real time
        if (viewport.interval - pygame.time.get_ticks()) <= 0:
            viewport.interval = pygame.time.get_ticks() + interval
            viewport.update(thing)
        
        ''' text printing '''
        com_name = text_main.render('DEATH CAPITAL',False, colors['main'])
        window.blit(com_name, ((scrx-com_name.size[0])/2,scry*0.05))

        window.blit(text_main.render(str(thing),False,colors['main']))

        window.blit(text_viewui.render(f'Zoom: x{viewport.max_val}',False, colors['main']), ((scrx+viewport.width+100)/2, scry*0.2))

        


        
        # outline
        pygame.draw.rect(window,colors['main'],pygame.Rect(((scrx-viewport.width)/2-outline_width,scrx*0.1-outline_width),(viewport.width+2*outline_width,viewport.height+2*outline_width)),width=outline_width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_d:
                    thing += 100
                if event.key == pygame.K_a:
                    thing -= 100
                if event.key == pygame.K_j:
                    viewport.scale(10)
                if event.key == pygame.K_k:
                    viewport.scale(-10)
                

        pygame.display.update()
        pygame.clock.tick(60)

game()