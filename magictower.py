# -*- coding: utf-8 -*-
import Library.draw as draw
import pygame
import time


def exec_game(game):
    global TIME_FLAG
    draw.init_interface(game)
    while game.indicator.get('win') is not True:
        t1 = time.process_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                game.process_event(event)
        time_flag = int((t1 - game.t0) * 24) % 24
        if time_flag != int((game.t1 - game.t0) * 24) % 24:
            game.t1 = t1
            draw.draw(game, time_flag)
    # draw.draw_end()


if __name__ == '__main__':
    pygame.init()
    while True:
        exec_game(draw.game)


# what else to do:
#   aircraft
#   alert
#   begin/end
#   restart
#   save/load
