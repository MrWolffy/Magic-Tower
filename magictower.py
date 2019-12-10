# -*- coding: utf-8 -*-
import json
from Library.draw import *
from Library.items import *
import os
import pygame
import time


def read_image():
    imglist = {}
    dirlist = os.listdir('UI')
    for dir in dirlist:
        if dir.endswith('.png'):
            imglist[dir[:-4]] = pygame.image.load('UI/' + dir)
    return imglist


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


if __name__ == '__main__':
    t0 = time.process_time()
    TIME_FLAG = 0
    tower_info = json.loads(''.join(open('Library/tower.json').readlines()))
    game = build_tower(tower_info)
    img_list = read_image()
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 10), 0, 32)
    init_interface(img_list, screen, game, TIME_FLAG)
    while True:
        t1 = time.process_time()
        delta_t = divmod(int((t1 - t0) * 3), 4)[1]
        if TIME_FLAG != delta_t:
            TIME_FLAG = delta_t
            draw_map(game.warrior.position[0], img_list, screen, game, TIME_FLAG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    game.warrior.move(event.key, game.map)
                    draw_map(game.warrior.position[0], img_list, screen, game, TIME_FLAG)
                    draw_info(game.warrior, img_list, screen, game)
                    # game.map.debug(game.warrior.position[0])
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()





