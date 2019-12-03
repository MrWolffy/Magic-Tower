import pygame
import os

if __name__ == '__main__':
    pygame.init()
    imglist = os.listdir('UI')
    wall_img = pygame.image.load('UI/Wall.png')
    screen = pygame.display.set_mode((640, 480), 0, 32)
    screen.blit(wall_img, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
