# -*- coding: utf-8 -*-
import pygame
from Library.items import *


def draw_rectangle_border(screen, point1, point2):
    rect = pygame.rect.Rect(point1, (point2[0] - point1[0], point2[1] - point1[1]))
    map_border = [(rect.left - 2, rect.top - 2),
                  (rect.right, rect.top - 2),
                  (rect.right, rect.bottom),
                  (rect.left - 2, rect.bottom)]
    pygame.draw.lines(screen, (190, 107, 39), True, map_border, 4)


def fill_rectangle(screen, point1, point2, img):
    rect = pygame.rect.Rect(point1, (point2[0] - point1[0], point2[1] - point1[1]))
    width = divmod(rect.width, 32)
    height = divmod(rect.height, 32)
    for i in range(width[0]):
        for j in range(height[0]):
            screen.blit(img, (rect.left + i * 32, rect.top + j * 32))
        if height[1] != 0:
            screen.blit(img.subsurface((0, 0), (32, height[1])),
                        (rect.left + i * 32, rect.top + height[0] * 32))


def draw_map(level, imglist, screen, game, time_flag):
    fill_rectangle(screen, (6 * 32, 32 + 5),
                   ((game.map.width + 5) * 32, ((game.map.height + 1) * 32 + 5)),
                   imglist['Floor'])
    for i in range(game.map.width):
        for j in range(game.map.height):
            temp_type = type(game.map.array[level][j][i])
            if temp_type.__name__ != 'Floor':
                if issubclass(temp_type, (Door, Warrior)):
                    screen.blit(imglist[temp_type.__name__].subsurface((0, 0), (32, 32)),
                                ((i + 6) * 32, (j + 1) * 32 + 5))
                elif issubclass(temp_type, Creature):
                    screen.blit(imglist[temp_type.__name__].subsurface((time_flag * 32, 0), (32, 32)),
                                ((i + 6) * 32, (j + 1) * 32 + 5))
                else:
                    screen.blit(imglist[temp_type.__name__], ((i + 6) * 32, (j + 1) * 32 + 5))
    pygame.display.update()


def draw_info_background(imglist, screen):
    # first
    draw_rectangle_border(screen, (32, 32 + 5), (5 * 32, 6 * 32 + 5))
    fill_rectangle(screen, (32, 32 + 5), (32 * 5, 32 * 6 + 5), imglist['Floor'])
    # second
    draw_rectangle_border(screen, (32, 6 * 32 + 5), (5 * 32, 10 * 32 + 8 + 5))
    fill_rectangle(screen, (32, 32 * 6 + 5), (32 * 5, 32 * 10 + 8 + 5), imglist['Floor'])
    pygame.draw.line(screen, (190, 107, 39), (32, 9 * 32 + 5 + 8), (5 * 32, 9 * 32 + 5 + 8), 4)
    # third
    draw_rectangle_border(screen, (32, 11 * 32 - 8), (5 * 32, 12 * 32 + 8))
    fill_rectangle(screen, (32, 11 * 32 - 8), (5 * 32, 12 * 32 + 8), imglist['Floor'])
    pygame.display.update()


def draw_info_content(warrior: Warrior, imglist, screen):
    arial_font = [None]
    for i in range(1, 33):
        arial_font.append(pygame.font.Font('Library/Arial.ttf', i))
    # first
    warrior_image = imglist['Warrior'].subsurface((0, 0), (32, 32))
    screen.blit(pygame.transform.scale(warrior_image, (40, 40)), (40, 40))
    info = arial_font[32].render(str(warrior.level), True, (255, 255, 255))
    screen.blit(info, (3 * 32, 44))
    info = arial_font[16].render(u'级', True, (255, 255, 255))
    screen.blit(info, (4 * 32 + 8, 62))
    info = [u'生命', u'攻击', u'防御', u'金币', u'经验']
    for i in range(len(info)):
        screen.blit(arial_font[16].render(info[i], True, (255, 255, 255)), (32 + 6, 2 * 32 + 28 + i * 20))
    info = arial_font[16].render(str(warrior.hp), True, (255, 255, 255))
    info_rect = info.get_rect()
    info_rect.center = (3.5 * 32 + 4, 3 * 32 + 8 + 0 * 20)
    screen.blit(info, info_rect)
    info = arial_font[16].render(str(warrior.attack), True, (255, 255, 255))
    info_rect = info.get_rect()
    info_rect.center = (3.5 * 32 + 4, 3 * 32 + 8 + 1 * 20)
    screen.blit(info, info_rect)
    info = arial_font[16].render(str(warrior.defense), True, (255, 255, 255))
    info_rect = info.get_rect()
    info_rect.center = (3.5 * 32 + 4, 3 * 32 + 8 + 2 * 20)
    screen.blit(info, info_rect)
    info = arial_font[16].render(str(warrior.gold), True, (255, 255, 255))
    info_rect = info.get_rect()
    info_rect.center = (3.5 * 32 + 4, 3 * 32 + 8 + 3 * 20)
    screen.blit(info, info_rect)
    info = arial_font[16].render(str(warrior.exp), True, (255, 255, 255))
    info_rect = info.get_rect()
    info_rect.center = (3.5 * 32 + 4, 3 * 32 + 8 + 4 * 20)
    screen.blit(info, info_rect)
    # second
    key_image = imglist['YellowKey']
    screen.blit(key_image, (32 + 4, 6 * 32 + 5 + 8))
    key_image = imglist['BlueKey']
    screen.blit(key_image, (32 + 4, 7 * 32 + 5 + 8))
    key_image = imglist['RedKey']
    screen.blit(key_image, (32 + 4, 8 * 32 + 5 + 8))
    info = arial_font[22].render(str(warrior.keys[0]), True, (255, 255, 255))
    info_rect = info.get_rect()
    info_rect.bottomright = (4 * 32, 7 * 32 + 5 + 6)
    screen.blit(info, info_rect)
    info = arial_font[22].render(str(warrior.keys[1]), True, (255, 255, 255))
    info_rect = info.get_rect()
    info_rect.bottomright = (4 * 32, 8 * 32 + 5 + 6)
    screen.blit(info, info_rect)
    info = arial_font[22].render(str(warrior.keys[2]), True, (255, 255, 255))
    info_rect = info.get_rect()
    info_rect.bottomright = (4 * 32, 9 * 32 + 5 + 6)
    screen.blit(info, info_rect)
    info = arial_font[16].render(u'个', True, (255, 255, 255))
    screen.blit(info, (4 * 32 + 12, 6 * 32 + 18))
    screen.blit(info, (4 * 32 + 12, 7 * 32 + 18))
    screen.blit(info, (4 * 32 + 12, 8 * 32 + 18))
    # third
    level = warrior.position[0]
    if level == 0:
        info = arial_font[16].render(u'序  章', True, (255, 255, 255))
        info_rect = info.get_rect()
        info_rect.center = (3 * 32, 9.5 * 32 + 5 + 8)
        screen.blit(info, info_rect)
    else:
        info = arial_font[16].render(u'第 ' + str(level) + u' 层', True, (255, 255, 255))
        info_rect = info.get_rect()
        info_rect.center = (3 * 32, 9.5 * 32 + 5 + 8)
        screen.blit(info, info_rect)
    # forth
    instruction1 = u'S 保存   Q 退出程序'
    instruction2 = u'A 读取   R 重新开始'
    screen.blit(arial_font[14].render(instruction1, True, (255, 255, 255)), (32 + 2, 11 * 32 - 6))
    screen.blit(arial_font[14].render(instruction2, True, (255, 255, 255)), (32 + 2, 12 * 32 - 16))
    pygame.display.update()


def draw_info(warrior, imglist, screen, game):
    draw_info_background(imglist, screen)
    draw_info_content(warrior, imglist, screen)


def init_interface(imglist, screen, game, time_flag):
    screen.fill((0, 0, 0))
    bg = pygame.image.load('UI/Background.png')
    fill_rectangle(screen, (0, 5), ((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 5), bg)
    draw_rectangle_border(screen, (6 * 32, 32 + 5), ((game.map.width + 6) * 32, (game.map.height + 1) * 32 + 5))
    draw_map(game.warrior.position[0], imglist, screen, game, time_flag)
    draw_info(game.warrior, imglist, screen, game)


