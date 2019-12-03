import json
from items import *
import os
import pygame


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
    screen.fill((0, 0, 0))
    for i in range(game.map.width):
        for j in range(game.map.height):
            screen.blit(imglist['Floor'], (i * 32, j * 32))
    pygame.display.update()
    for i in range(game.map.width):
        for j in range(game.map.height):
            if type(game.map.array[level][j][i]).__name__ != 'Floor':
                screen.blit(imglist[type(game.map.array[0][j][i]).__name__], (i * 32, j * 32))
    pygame.display.update()


def init_interface(imglist):
    dirlist = os.listdir('UI')
    for dir in dirlist:
        if dir.endswith('.png'):
            imglist[dir[:-4]] = pygame.image.load('UI/' + dir)
    draw_map(0)


if __name__ == '__main__':
    tower_info = json.loads(open('tower.txt').readline())
    game = build_tower(tower_info)
    imglist = {}
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((game.map.width * 32, game.map.height * 32), 0, 32)
    init_interface(imglist)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    game.warrior.move(event.key, game.map)
                    draw_map(game.warrior.position[0])






