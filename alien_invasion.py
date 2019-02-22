import sys
import pygame

from settings import Settings
from ship import Ship

import game_functions as gf

def run_game():
    pygame.init()

    ai_setting = Settings() #实例一个设置类对象

    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_heigh))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_setting,screen)
    #开始游戏主循环
    while(True):     
        gf.check_events(ship) 
        ship.update()   
        gf.update_screen(ai_setting,screen,ship)
    

run_game()