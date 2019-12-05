# -*- coding: utf-8 -*-
import json
from items import *
import os
import pygame
import time


t0 = time.process_time()
TIME_FLAG = 0


def build_tower(tower_info):
    tower_structure = tower_info['tower_structure']
    item_info = tower_info['item_info']
    level = tower_structure['total_level']
    height = tower_structure['height']
    width = tower_structure['width']
    map = Container(level, height, width)
    for i in range(level):
        for j in range(height):
            for k in range(width):
                map.array[i][j][k] = \
                    eval(tower_structure['level_structure'][i][j][k] + '(item_info)')
    warrior_position = item_info['Warrior']['position']
    warrior = map.array[warrior_position[0]][warrior_position[1]][warrior_position[2]]
    game = Game(map, warrior)
    return game


def draw_map(level):
    global TIME_FLAG
    for i in range(game.map.width):
        for j in range(game.map.height):
            screen.blit(imglist['Floor'], ((i + 6) * 32, (j + 1) * 32 + 5))
    pygame.display.update()
    for i in range(game.map.width):
        for j in range(game.map.height):
            temp_type = type(game.map.array[level][j][i])
            if temp_type.__name__ != 'Floor':
                if issubclass(temp_type, (Door, Warrior)):
                    screen.blit(imglist[temp_type.__name__].subsurface((0, 0), (32, 32)),
                                ((i + 6) * 32, (j + 1) * 32 + 5))
                elif issubclass(temp_type, Creature):
                    screen.blit(imglist[temp_type.__name__].subsurface((TIME_FLAG * 32, 0), (32, 32)),
                                ((i + 6) * 32, (j + 1) * 32 + 5))
                else:
                    screen.blit(imglist[temp_type.__name__], ((i + 6) * 32, (j + 1) * 32 + 5))
    pygame.display.update()


def init_interface(imglist):
    screen.fill((0, 0, 0))
    bg = pygame.image.load('UI/Background.png')
    for i in range(game.map.width + 7):
        for j in range(game.map.height + 2):
            screen.blit(bg, (i * 32, j * 32 + 5))
    map_border = [(6 * 32, 32 + 5),
                  ((game.map.width + 6) * 32, 32 + 5),
                  ((game.map.width + 6) * 32, (game.map.height + 1) * 32 + 5),
                  (6 * 32, (game.map.height + 1) * 32 + 5)]
    pygame.draw.lines(screen, (190, 107, 39), True, map_border, 5)
    draw_map(0)


if __name__ == '__main__':
    tower_info = json.loads(''.join(open('tower.txt').readlines()))
    game = build_tower(tower_info)
    imglist = {}
    dirlist = os.listdir('UI')
    for dir in dirlist:
        if dir.endswith('.png'):
            imglist[dir[:-4]] = pygame.image.load('UI/' + dir)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 10), 0, 32)
    init_interface(imglist)
    while True:
        t1 = time.process_time()
        delta_t = divmod(int((t1 - t0) * 3), 4)[1]
        if TIME_FLAG != delta_t:
            TIME_FLAG = delta_t
            draw_map(game.warrior.position[0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    game.warrior.move(event.key, game.map)
                    draw_map(game.warrior.position[0])
                    # game.map.debug(game.warrior.position[0])
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()






