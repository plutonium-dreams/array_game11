'''
trading engine
'''
import pygame, os
import numpy as np
# import pandas as pd
from defaults import *
from utils import *

class Trade():
    def __init__(self, balance):
        # vars
        self.balance = balance
        self.share = 0
        self.value = 1
        self.price = 0

        self.bet = 0
        self.power = 2

        # buttons
        self.button_buy = Button((825+70,650-30), (100,50), 'Buy', 'click')
        self.button_sell = Button((825-70,650-30), (100,50), 'Sell', 'click')
        
        self.button_add = Button((915,650-95), (50,50), '+', 'click')
        self.button_min = Button((735,650-95), (50,50), '-', 'click')

        self.button_exp = Button((855,650-95), (50,50), 'x10', 'click')
        self.button_log = Button((795,650-95), (50,50), '/10', 'click')

        self.BUTTONS = np.array([self.button_buy,self.button_sell,self.button_add,self.button_min, self.button_exp, self.button_log])

        ''' add the trading system here; formalize '''


    def render(self, window):
        for button in self.BUTTONS:
            button.render(window)
        
        # blits the current bet
        curr_bet = text_dash.render(str(self.bet), False, colors['ui'])
        pos_bet = (825-curr_bet.width/2,650-165)
        pygame.draw.rect(window, colors['bg_light'], ((pos_bet[0]-10,pos_bet[1]),(curr_bet.width+20,curr_bet.height+5)))
        window.blit(curr_bet, pos_bet)
        # blits the current power of 10
        curr_pow = text_dash.render(f'{self.power}',False,colors['text'])
        window.blit(curr_pow, (825-curr_pow.width/2,620-curr_pow.height/2))

        # blits the current balance
        text_bal = text_dash.render(f'Balance: ${self.balance}', False, colors['ui'])
        window.blit(text_bal, (705,355))
        # blits the current share
        text_shr = text_dash.render(f'Shares: {round(self.share,5)}', False, colors['ui'])
        window.blit(text_shr, (705,355+text_shr.height))
        # blits the current dollar value of share
        text_val = text_dash.render(f'Val: ${self.value}', False, colors['ui'])
        window.blit(text_val, (705,355+text_shr.height+text_val.height))
        # blits the current share price
        text_pri = text_dash.render(f'Price: ${round(self.price)}', False, colors['ui'])
        window.blit(text_pri, (705,355+text_shr.height+text_val.height+text_pri.height))


    def update(self, price):
        for button in self.BUTTONS:
            button.update()

        self.price = price
        self.value = round(self.price*self.share)

        # bet config
        if self.button_add.state:
            self.bet = int(np.round(self.bet,-2))
            new_bet = self.bet + 10**self.power
            if new_bet < 1000000:
                self.bet = new_bet
            else:
                self.bet = 1000000
        elif self.button_min.state:
            new_bet = self.bet - 10**self.power
            if new_bet < 0:
                self.bet = 0
            else:
                self.bet = new_bet
        elif self.button_exp.state and self.power < 5:
            self.power += 1
        elif self.button_log.state and self.power > 2:
            self.power -= 1

        if self.button_buy.state:
            if self.bet <= self.balance:
                self.buy(self.bet)
                self.bet = 0
            else:
                self.bet = self.balance
        elif self.button_sell.state:
            if self.bet <= self.value:
                self.sell(self.bet)
                self.bet = 0
            else:
                self.bet = self.value

    # how tf do you buy and sell with shares
    def buy(self, amt):
        self.balance-=amt
        self.share+=amt/self.price
    
    def sell(self, amt):
        new_share = self.share - amt/self.price
        if new_share < 0:
            self.share = 0
            self.balance += amt
        else:
            self.share -= amt/self.price
            self.balance += amt
        


