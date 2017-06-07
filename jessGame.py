#!/usr/bin/env python3
#by Jess Weichler
#thanks to Seth Kenlon

import pygame #load pygame keywords
import sys
import os

'''OBJECTS'''
#put classes & functions here

class Player(pygame.sprite.Sprite):
    #spawn a player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', 'hero.png')).convert()
        self.rect = self.image.get_rect()
                

'''SETUP'''
#code runs once

screenX = 960 #width
screenY = 720 #height

fps = 40 #frame rate
afps = 4 #animation cycles
clock = pygame.time.Clock()
pygame.init()

main = True

screen = pygame.display.set_mode([screenX, screenY])
backdrop = pygame.image.load(os.path.join('images','stage.png')).convert()
backdropRect = screen.get_rect()

player = Player() #spawn player
player.rect.x = 0
player.rect.y = 0
movingsprites = pygame.sprite.Group()
movingsprites.add(player)



'''MAIN LOOP'''
#code runs many times

while main == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    screen.blit(backdrop, backdropRect) #if you have backdrop
    #screen.fill(black) #if you don't have backdrop

    pygame.display.flip()
    clock.tick(fps)
    
    

            





    



