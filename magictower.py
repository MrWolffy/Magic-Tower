import json
from items import *
import sys, os
from pynput.keyboard import Controller, Key, Listener
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


def on_press(key, game):
    try:
        game.warrior.move(key, game.map)
        print('\b' * 1000, end='')
        game.map.debug()
    except AttributeError:
        game.warrior.move(key, game.map)
        print('\b' * 1000, end='')
        game.map.debug()


def on_release(key):
    if key == Key.esc:
        return False


def start_listen(game):
    with Listener(on_press=lambda key: on_press(key, game)) as listener:
        listener.join()


if __name__ == '__main__':
    tower_info = json.loads(open('tower.txt').readline())
    game = build_tower(tower_info)
    game.map.debug()
    kb = Controller()
    start_listen(game)




