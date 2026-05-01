'''
Math 154 Final Project
Group Mayad

BLACK CAPITAL, INC.
A social commentary

Main Module
Description: The main process of the game. Handles player input and pygame backend.

NOTES
To do:
[ ] implement the market system
    [/] moving graph
    [ ] add viewport utilities
        [/] zoom and shi
        [ ] make it so that when you zoom in gadamo ang markers
    [/] graph that moves according to principles of the stock market
        [ ] the long-term and short-term factorsk
[ ] implement player input
    [ ] buy and sell mechanic
    [ ] make the buy sell mechanic affect the stock market
[ ] implement events into the game
    [ ] implement a text engine in the game
    [ ] random events:
        [ ] war
        [ ] pandemic
        [ ] coup
        [ ] technology
[ ] basic gameloop
    [ ] return the seed from the random module so that pwede mareproduce ang states
    [ ] player is able to bet on the stock market
    [ ] events can happen + implementation of potential sources of infos
[ ] add a title screen


currency in dollars?
setting?
time period?
'''
import pygame, random, os, sys
import numpy as np 
import sympy as sp
from defaults import *
from utils import *
from graph import *
from trade import *
from market import *

pygame.init()

window = pygame.display.set_mode((scrx, scry))
pygame.clock = pygame.time.Clock()
pygame.display.set_caption('BLACK MARKET')

np.random.seed(1)

viewport = Viewport()



trade = Trade()

def game():
    thing  = 0
    progress = 0
    
    bet = 0
    
    
    level = 10000
    money = 1000
    shares = 0

    market = Market(level)

    while True:
        window.fill(colors['bg'])
        
        market.update()
    
        trade.render(window)
        
        viewport.draw(colors['main'])
        viewport.render(window)
        trade.update()                


        pygame.draw.rect(window, colors['ui'], pygame.Rect(((scrx-viewport.width)/2-outline_width, scry/20),((viewport.interval - pygame.time.get_ticks())/(2*interval/1000),10)))
    
        # if real time
        
        if (viewport.interval - pygame.time.get_ticks()) <= 0:
            viewport.interval = pygame.time.get_ticks() + interval
            viewport.update(market.gen_points())

            # calculate new price of shares
            shares *= viewport.processed_vals[-2]/viewport.processed_vals[-1]
            shares = round(shares)
            if shares < -bet:
                bet = -shares
        
        ''' text printing '''
        com_name = text_main.render('DEATH CAPITAL',False, colors['main'])
        window.blit(com_name, ((scrx-com_name.size[0])/2,viewport.pos[1]-50))

        window.blit(text_main.render(str(thing),False,colors['ui']))


        # I thought making the in game zoom value be a whole number would be nice
        window.blit(text_viewui.render(f'Zoom: x{(viewport.view_height-100)/1000}',False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+50))

        window.blit(text_viewui.render(f'Number of points:{viewport.view_length}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1))

        window.blit(text_viewui.render(f'GBM Model Values', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+125))
        
        window.blit(text_viewui.render(f'Ann. Yield (mu): {market.mu*market.time_horizon}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+150))
        window.blit(text_viewui.render(f'Vol.(sigma): {market.sigma}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+175))

        window.blit(text_viewui.render(f'Buy: {bet}' if bet>=0 else f'Sell: {-bet}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+225))

        window.blit(text_viewui.render(f'Bank: ${money}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+250))
        
        window.blit(text_viewui.render(f'Shares: ${shares}', False, colors['ui']), (scrx/2-viewport.width+25, scry*0.1+275))

        # outline
        pygame.draw.rect(window,colors['main'],pygame.Rect(((scrx-viewport.width)/2-outline_width,scrx*0.1-outline_width),(viewport.width+2*outline_width,viewport.height+2*outline_width)),width=outline_width)
        
        pygame.draw.circle(window, 'white', (scrx/2,scry/2), 5)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                # market.graph()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_w and not viewport.follow:
                    viewport.translate(1)
                if event.key == pygame.K_s and not viewport.follow:
                    viewport.translate(-1)
                
                if event.key == pygame.K_d:
                    market.mu += 0.01
                if event.key == pygame.K_a:
                    market.mu -= 0.01
                if event.key == pygame.K_e:
                    market.sigma += 0.001
                if event.key == pygame.K_q:
                    market.sigma -= 0.001
                
                # Corrected the keybinds for the zoom in zoom out of the y axis to match that of the x axis
                # Also simplified the scale_y method

                if event.key == pygame.K_j and viewport.view_height > 1000:
                    viewport.scale_y(-10)
                if event.key == pygame.K_k and viewport.view_height < viewport.max_view_height:
                    viewport.scale_y(10)
                    

                ''' modify x_scale to account for 252 trading days '''
                if event.key == pygame.K_u and viewport.view_length > 5:
                    viewport.scale_x(-5)
                if event.key == pygame.K_i and viewport.view_length < viewport.max_view_length:
                    viewport.scale_x(5)

                if event.key == pygame.K_h:
                    # you can move this code to the viewport class blueprint if you want to make this more organized
                    # add limits
                    if viewport.follow:
                        viewport.translation = viewport.y_vals[-1]
                        viewport.follow = False
                        viewport.surface.fill(colors['bg'])
                    else:
                        viewport.follow = True
                        viewport.surface.fill(colors['bg'])
                
                ''' trading controls '''
                # fix buy and sell
                if event.key == pygame.K_TAB:
                    # add a way to make it switch between buy and sell
                    pass
                    
                if event.key == pygame.K_EQUALS:
                    bet += 100
                if event.key == pygame.K_MINUS:
                    # if -bet >= shares-100:
                    #     bet = -np.round(shares,-len(str(shares)))
                    if -bet < shares - 100:
                        bet -= 100
                    
                if event.key == pygame.K_RETURN:
                    market = Market(level + bet)
                    level += bet

                    if bet > 0:
                        money -= bet
                        shares += bet
                    elif bet < 0:
                        money -= bet
                        shares += bet

                
                # if event.key == pygame.K_SPACE:
                #     print(market.output)
                
        print(shares, bet)
        pygame.display.update()
        pygame.clock.tick(60)
        pygame.display.set_caption(f'BLACK MARKET {pygame.clock.get_fps()}')

game()