# -*- coding: utf-8 -*-
import Library.draw as draw
from Library.items import game
import pygame
import time


def exec_game(game):
    draw.draw_begin()
    while game.status['win'] is not True:
        t1 = time.process_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                game.process_event(event)
        time_flag = int((t1 - game.t0) * 24)
        if time_flag != int((game.t1 - game.t0) * 24):
            game.t1 = t1
            draw.draw(game, time_flag)
    draw.draw_end()


if __name__ == '__main__':
    pygame.init()
    draw.init_interface(game)
    while True:
        exec_game(game)


# what else to do:
#   alert
