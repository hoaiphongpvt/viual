import pygame, sys
from settings import *
from level import Level
from menu import *
from player import *
from game import *

pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('PS Platformer')
clock = pygame.time.Clock()
title_music = pygame.mixer.Sound('audio/music.wav')
title_music.play(loops = -1)

g = Game()

while g.running:
    g.curr_menu.display_menu()
    title_music.stop()
    g.game_loop() 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)