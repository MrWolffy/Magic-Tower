# -*- coding: utf-8 -*-
import Library.draw as draw
from Library.items import game
import pygame
import time


def exec_game(game):
    draw.draw_begin()
    keys_down = {}
    while game.status['win'] is not True:
        t1 = time.process_time()
        # 获取键盘动作，计算当前在按着的键
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                keys_down[event.key] = [t1, t1]
                # 第一个时间是按键动作发生时间，第二个时间是上一次响应时间
            elif event.type == pygame.KEYUP:
                if event.key in keys_down:
                    keys_down.pop(event.key)
        # 对当前在按着的键循环
        for key in keys_down.items():
            if t1 - key[1][0] < 0.05:
                # 只要按键立刻响应
                game.process_event(key[0])
            elif t1 - key[1][0] > 0.5 and t1 - key[1][1] > 0.1:
                # 按键大于0.5秒判断为长按，每隔0.1秒响应一次
                game.process_event(key[0])
                key[1][1] = t1
        # 画图的速度是每秒24帧
        time_flag = int((t1 - game.t0) * 24)
        if time_flag != int((game.t1 - game.t0) * 24):
            game.t1 = t1
            game.process_next_frame()
            draw.draw(game, time_flag)
    draw.draw_end()
    game.status['win'] = False
    game.process_load('Library/tower.json')


if __name__ == '__main__':
    pygame.init()
    draw.init_interface(game)
    while True:
        exec_game(game)

