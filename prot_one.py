''' prototypr idea #1 for math 154 fproj '''
import pygame, random, os, sys
import numpy as np 
import sympy as sp

pygame.init()

scrx, scry = (800,600)

window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()
pygame.display.set_caption('Prototype Game')

viewport = pygame.Surface((400,300))

ratio = (viewport.get_width()/scrx,viewport.get_height()/scry)
outline_width = 5

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    coords.pop()

        window.fill('black')
        viewport.fill('black')
        pygame.draw.rect(window,'white',pygame.Rect(((scrx-viewport.get_width())/2-outline_width,scrx*0.1-outline_width),(viewport.get_width()+2*outline_width,viewport.get_height()+2*outline_width)),width=outline_width)

        # coords








        window.blit(viewport,((scrx-viewport.get_width())/2,scrx*0.1))

        pygame.display.update()
        pygame.clock.tick(60)

game()