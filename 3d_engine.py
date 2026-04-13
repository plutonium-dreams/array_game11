''' 
prototypr idea #1 for math 154 fproj 

base template
'''
import pygame, random, os, sys, math
import numpy as np 
import sympy as sp

pygame.init()

scrx, scry = (500,500)

window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()
pygame.display.set_caption('Prototype Game')


size = 10
       
# p = (x,y)

def point(p):
    pygame.draw.rect(window, 'white', ((p[0]-size/2,p[1]-size/2),(size,size)))

def screen(p):
    point = ((p[0] + 1)/2 * scrx, (1-(p[1] + 1)/2) * scry)
    return point 

def project(p3d):
    point_3d = (p3d[0]/p3d[2], p3d[1]/p3d[2])
    return point_3d

def translate_z(p3d, dz):
    point_3d = (p3d[0], p3d[1], p3d[2] + dz)
    return point_3d

def rotate_xz(p3d, angle):
    point_3d = (
        p3d[0]*math.cos(angle) - p3d[2]*math.sin(angle),
        p3d[1],
        p3d[0]*math.sin(angle) + p3d[2]*math.cos(angle),
    )
    return point_3d

def line(p1, p2):
    pygame.draw.line(window, 'white', p1, p2)

vertices = [
    (0.25,0.25,0.25),
    (-0.5,0.25,0.25),
    (-0.25,-0.5,0.25),
    (0.25,-0.25,0.25),

    (0.25,0.5,-0.25),
    (-0.25,0.25,-0.25),
    (-0.25,-0.25,-0.25),
    (0.5,-0.25,-0.25),

    (0.5,0.5,0.25),
]

faces = [
    [0,1,2,3],
    [4,5,6,7],
    [0,4],
    [1,5],
    [2,6],
    [3,7],
    [7,8]
]


def game():
    dt = 1/60
    dz = 1
    angle = 0
    rotate = 0
    zoom = 0

    while True:
        window.fill('black')
        
        # render vertices
        for v in vertices:
            point(screen(project(translate_z(rotate_xz(v, angle),dz))))

        # render wireframe
        for f in faces:
            for i in range(len(f)):
                a = vertices[f[i]]
                b = vertices[f[(i+1)%len(f)]]
                
                line(screen(project(translate_z(rotate_xz(a, angle),dz))), screen(project(translate_z(rotate_xz(b, angle),dz))))

        # dz += 1 * dt

        if rotate:
            angle += math.pi * dt * rotate

        if zoom:
            dz += 1 * dt * zoom

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if rotate:
                        rotate = 0
                    else:
                        rotate = 1
                if event.key == pygame.K_a:
                    if rotate:
                        rotate = 0
                    else:
                        rotate = -1
                
                if event.key == pygame.K_j:
                    if zoom:
                        zoom = 0
                    else:
                        zoom = -1
                if event.key == pygame.K_k:
                    if zoom:
                        zoom = 0
                    else:
                        zoom = 1
                    


        pygame.display.update()
        pygame.clock.tick(60)

game()