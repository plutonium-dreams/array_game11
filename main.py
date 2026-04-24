'''
Math 154 Final Project
Black Market

To do:
[ ] implement the market system
    [/] moving graph
    [ ] add viewport utilities
        [/] zoom and shi
        [ ] make it so that when you zoom in gadamo ang markers
    [ ] graph that moves according to principles of the stock market
        [ ] the long-term and short-term factorsk
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
        
        viewport.draw([])
        viewport.render(window)
    
        # if real time
        if (viewport.interval - pygame.time.get_ticks()) <= 0:
            viewport.interval = pygame.time.get_ticks() + interval
            viewport.update(thing)
        
        ''' text printing '''
        com_name = text_main.render('DEATH CAPITAL',False, colors['main'])
        window.blit(com_name, ((scrx-com_name.size[0])/2,viewport.pos[1]-50))

        window.blit(text_main.render(str(thing),False,colors['ui']))


        # I thought making the in game zoom value be a whole number would be nice
        window.blit(text_viewui.render(f'Zoom: x{(viewport.max_val-1000)/10000}',False, colors['ui']), ((scrx+viewport.width+50)/2, scry*0.2))

        window.blit(text_viewui.render(f'Number of points:{viewport.view_length}', False, colors['ui']), ((scrx+viewport.width+50)/2, scry*0.1))

        


        
        # outline
        pygame.draw.rect(window,colors['main'],pygame.Rect(((scrx-viewport.width)/2-outline_width,scrx*0.1-outline_width),(viewport.width+2*outline_width,viewport.height+2*outline_width)),width=outline_width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_w and viewport.follow:
                    viewport.translate(1)
                if event.key == pygame.K_s and viewport.follow:
                    viewport.translate(-1)
                if event.key == pygame.K_d:
                    thing += 100
                if event.key == pygame.K_a:
                    thing -= 100
                
                # Corrected the keybinds for the zoom in zoom out of the y axis to match that of the x axis
                # Also simplified the scale_y method

                if event.key == pygame.K_j and viewport.max_val > 1000:
                    viewport.scale_y(-10)
                if event.key == pygame.K_k and viewport.max_val < viewport.ciel:
                    viewport.scale_y(10)
                if event.key == pygame.K_u and viewport.view_length > 5:
                    viewport.scale_x(-1)
                if event.key == pygame.K_i and viewport.view_length < 51:
                    viewport.scale_x(1)

                if event.key == pygame.K_h:
                    # you can move this code to the viewport class blueprint if you want to make this more organized
                    if viewport.follow:
                        viewport.translation = viewport.y_vals[-1]
                        viewport.follow = False
                        viewport.surface.fill(colors['bg'])
                    else:
                        viewport.follow = True
                        viewport.surface.fill(colors['bg'])
                

        pygame.display.update()
        pygame.clock.tick(60)
        pygame.display.set_caption(f'BLACK MARKET {pygame.clock.get_fps()}')

game()