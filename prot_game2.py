import pygame, random, os, sys
import numpy as np 
import sympy as sp

pygame.init()

scrx, scry = (800,600)

window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()
pygame.display.set_caption('Prototype Game')

# points to plot
x = sp.symbols('x')
f = sp.lambdify(x, sp.sin(x))

viewport = pygame.Surface((400,300))





def game():
    view_scale = 0.5
    view_x,view_y = scrx/2,scry/2
    resolution = 3

    ratio = (viewport.get_width()/scrx,viewport.get_height()/scry)
    
    while True:
        window.fill('black')
        viewport.fill('black')
        
        # draw markings
        pygame.draw.line(viewport, 'white', (0,view_y*ratio[1]),(scrx*ratio[0],view_y*ratio[1]))     # x-axis
        pygame.draw.line(viewport, 'white', (view_x*ratio[0],0),(view_x*ratio[0],scry*ratio[1]))     # y-axis

        # draw the graph
    
        x_vals = np.linspace(-resolution,resolution+50,scrx)
        y_vals = f(x_vals)

        coords = []
        for i in range(len(x_vals)):
            coords.append((int(x_vals[i]*view_scale*(scrx/x_vals[-1])*ratio[0])+view_x*ratio[0], int(-y_vals[i]*view_scale*(scrx/y_vals[-1])*ratio[1])+view_y*ratio[1]))

        pygame.draw.lines(viewport,'green',False,coords)

        pygame.draw.rect(window,'white',pygame.Rect((-5+(scrx-viewport.get_width())/2,-5+scry*0.1),(viewport.get_width()+10,viewport.get_height()+10)), width=5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    view_y += 50
                if event.key == pygame.K_s:
                    view_y -= 50
                if event.key == pygame.K_a:
                    view_x += 50
                if event.key == pygame.K_d:
                    view_x -= 50

                if event.key == pygame.K_j and view_scale > 0.2:
                    view_scale -= 0.1
                if event.key == pygame.K_k:
                    view_scale += 0.1

                if event.key == pygame.K_u and resolution > 1:
                    resolution -= 1
                if event.key == pygame.K_i:
                    resolution += 1
                    
        window.blit(viewport,((scrx-viewport.get_width())/2,scry*0.1))
        pygame.display.update()
        pygame.clock.tick(60)


game()
