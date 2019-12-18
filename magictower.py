# -*- coding: utf-8 -*-
from Library.draw import *
import pygame
import time


def build_tower(tower_info):
    tower_structure = tower_info['tower_structure']
    creature_info = tower_info['creature_info']
    level = tower_structure['total_level']
    height = tower_structure['height']
    width = tower_structure['width']
    map = Container(level, height, width)
    for i in range(level):
        for j in range(height):
            for k in range(width):
                # print(i, j, k)
                map.array[i][j][k] = \
                    eval(tower_structure['level_structure'][i][j][k] +
                         '(creature_info, [' + str(i) + ', ' + str(j) + ', ' + str(k) + '])')
    warrior_position = creature_info['Warrior']['position']
    warrior = map.array[warrior_position[0]][warrior_position[1]][warrior_position[2]]
    game = Game(map, warrior)
    return game


if __name__ == '__main__':
    global TIME_FLAG
    game = build_tower(info)
    add_additional_function(game)
    # game.map.array = [game.map.array[0], game.map.array[11]]
    pygame.init()
    init_interface(game)
    while True:
        t1 = time.process_time()
        delta_t = divmod(int((t1 - t0) * 3), 4)[1]
        if TIME_FLAG != delta_t:
            TIME_FLAG = delta_t
            draw_map(game.map.array[game.warrior.position[0]], TIME_FLAG)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    game.warrior.move(event.key, game)
                    draw_map(game.map.array[game.warrior.position[0]], TIME_FLAG)
                    draw_info(game)
                    # game.map.debug(game.warrior.position[0])
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_a:
                    pass
                elif event.key == pygame.K_s:
                    pass
                elif event.key == pygame.K_r:
                    pass
                elif event.key == pygame.K_l:
                    if game.indicator.get('warrior_get_detector'):
                        draw_detector_info(game)
                elif event.key == pygame.K_j:
                    pass
            time.sleep(0.01)





