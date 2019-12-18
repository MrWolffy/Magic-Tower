# -*- coding: utf-8 -*-
import os
import pygame
from Library.items import *

arial_font = [None]
screen = None
TIME_FLAG = 0
t0 = time.process_time()


def read_image():
    imglist = {}
    dirlist = os.listdir('UI')
    for dir in dirlist:
        if dir.endswith('.png'):
            imglist[dir[:-4]] = pygame.image.load('UI/' + dir)
    return imglist


img_list = read_image()


def draw_rectangle_border(point1, point2):
    rect = pygame.rect.Rect(point1, (point2[0] - point1[0], point2[1] - point1[1]))
    map_border = [(rect.left - 2, rect.top - 2),
                  (rect.right, rect.top - 2),
                  (rect.right, rect.bottom),
                  (rect.left - 2, rect.bottom)]
    pygame.draw.lines(screen, (190, 107, 39), True, map_border, 4)


def fill_rectangle(point1, point2, img):
    rect = pygame.rect.Rect(point1, (point2[0] - point1[0], point2[1] - point1[1]))
    width = divmod(rect.width, 32)
    height = divmod(rect.height, 32)
    for i in range(width[0]):
        for j in range(height[0]):
            screen.blit(img, (rect.left + i * 32, rect.top + j * 32))
            if width[1] != 0:
                screen.blit(img.subsurface((0, 0), (width[1], 32)),
                            (rect.left + width[0] * 32, rect.top + j * 32))
        if height[1] != 0:
            screen.blit(img.subsurface((0, 0), (32, height[1])),
                        (rect.left + i * 32, rect.top + height[0] * 32))
    if width[1] != 0 and height[1] != 0:
        screen.blit(img.subsurface((0, 0), (width[1], height[1])),
                    (rect.left + width[0] * 32, rect.top + height[0] * 32))


def print_string(string, fontsize, topleft=(0, 0), center=None):
    info = arial_font[fontsize].render(string, True, (255, 255, 255))
    if center is None:
        screen.blit(info, topleft)
    else:
        info_rect = info.get_rect()
        info_rect.center = center
        screen.blit(info, info_rect)


def draw_map(level, time_flag):
    width = len(level[0])
    height = len(level)
    fill_rectangle((6 * 32, 32 + 5), ((width + 6) * 32, ((height + 1) * 32 + 5)), img_list['Floor'])
    for i in range(width):
        for j in range(height):
            temp_type = type(level[j][i])
            if temp_type.__name__ != 'Floor':
                if issubclass(temp_type, (Door, Warrior)):
                    screen.blit(img_list[temp_type.__name__].subsurface((0, 0), (32, 32)),
                                ((i + 6) * 32, (j + 1) * 32 + 5))
                elif issubclass(temp_type, (Creature, Lava, Star)):
                    screen.blit(img_list[temp_type.__name__].subsurface((time_flag * 32, 0), (32, 32)),
                                ((i + 6) * 32, (j + 1) * 32 + 5))
                else:
                    screen.blit(img_list[temp_type.__name__], ((i + 6) * 32, (j + 1) * 32 + 5))
    pygame.display.update()


def draw_info_background():
    # first
    draw_rectangle_border((32, 32 + 5), (5 * 32, 6 * 32 + 5))
    fill_rectangle((32, 32 + 5), (32 * 5, 32 * 6 + 5), img_list['Floor'])
    # second
    draw_rectangle_border((32, 6 * 32 + 5), (5 * 32, 10 * 32 + 8 + 5))
    fill_rectangle((32, 32 * 6 + 5), (32 * 5, 32 * 10 + 8 + 5), img_list['Floor'])
    pygame.draw.line(screen, (190, 107, 39), (32, 9 * 32 + 5 + 8), (5 * 32, 9 * 32 + 5 + 8), 4)
    # third
    draw_rectangle_border((32, 11 * 32 - 8), (5 * 32, 12 * 32 + 8))
    fill_rectangle((32, 11 * 32 - 8), (5 * 32, 12 * 32 + 8), img_list['Floor'])
    pygame.display.update()


def draw_info_content(warrior: Warrior):
    # first
    warrior_image = img_list['Warrior'].subsurface((0, 0), (32, 32))
    screen.blit(pygame.transform.scale(warrior_image, (40, 40)), (40, 40))
    print_string(str(warrior.level), 32, (3 * 32, 44))
    print_string(u'级', 16, (4 * 32 + 8, 62))
    info = [u'生命', u'攻击', u'防御', u'金币', u'经验']
    for i in range(len(info)):
        print_string(info[i], 16, (32 + 6, 2 * 32 + 28 + i * 20))
    print_string(str(warrior.hp), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 0 * 20))
    print_string(str(warrior.attack), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 1 * 20))
    print_string(str(warrior.defense), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 2 * 20))
    print_string(str(warrior.gold), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 3 * 20))
    print_string(str(warrior.exp), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 4 * 20))
    # second
    key_image = img_list['YellowKey']
    screen.blit(key_image, (32 + 4, 6 * 32 + 5 + 8))
    key_image = img_list['BlueKey']
    screen.blit(key_image, (32 + 4, 7 * 32 + 5 + 8))
    key_image = img_list['RedKey']
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
        print_string(u'序  章', 16, center=(3 * 32, 9.5 * 32 + 5 + 8))
    else:
        print_string(u'第 ' + str(level) + u' 层', 16, center=(3 * 32, 9.5 * 32 + 5 + 8))
    # forth
    print_string(u'S 保存   Q 退出程序', 14, (32 + 2, 11 * 32 - 6))
    print_string(u'A 读取   R 重新开始', 14, (32 + 2, 12 * 32 - 16))
    pygame.display.update()


def draw_info(game):
    draw_info_background()
    draw_info_content(game.warrior)


def init_interface(game, time_flag):
    global screen
    screen = pygame.display.set_mode(((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 10), 0, 32)
    screen.fill((0, 0, 0))
    bg = pygame.image.load('UI/Background.png')
    for i in range(1, 33):
        arial_font.append(pygame.font.Font('Library/Arial.ttf', i))
    fill_rectangle((0, 5), ((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 5), bg)
    draw_rectangle_border((6 * 32, 32 + 5), ((game.map.width + 6) * 32, (game.map.height + 1) * 32 + 5))
    draw_map(game.map.array[game.warrior.position[0]], time_flag)
    draw_info(game)


def speak(item, content, game: items.Game):
    def adjust_pos(pos):
        rect = pygame.rect.Rect((0, 0), (7.5 * 32, 2 * 32 + 8))
        rect.center = ((pos[1] + 6.5) * 32, ((pos[0] + 1.5) * 32 + 5))
        return rect

    global TIME_FLAG, t0
    pos = adjust_pos((item.position[1], item.position[2]))
    content = content.split('\t')
    while True:
        t1 = time.process_time()
        delta_t = divmod(int((t1 - t0) * 3), 4)[1]
        if TIME_FLAG != delta_t:
            TIME_FLAG = delta_t
            draw_map(game.map.array[item.position[0]], TIME_FLAG)
        draw_rectangle_border(pos.topleft, pos.bottomright)
        fill_rectangle(pos.topleft, pos.bottomright, pygame.image.load('UI/Floor.png'))
        print_string(info['item_info'][type(item).__name__]['chinese_name'] + ':',
                     16, (pos.left + 48, pos.top + 5))
        for i in range(len(content)):
            print_string(content[i], 14, (pos.left + 48, pos.top + 24 + 14 * i))
        if type(item).__name__ != 'Warrior':
            screen.blit(img_list['Floor'], (pos.left + 5, pos.top + 5))
            screen.blit(img_list[type(item).__name__].subsurface((divmod(int((t1 - t0) * 3), 4)[1] * 32, 0), (32, 32)),
                        (pos.left + 5, pos.top + 5))
        else:
            screen.blit(img_list[type(item).__name__].subsurface((0, 0), (32, 32)),
                        (pos.left + 5, pos.top + 5))
        string = arial_font[10].render('-- Space --', True,
                                       (255 * (math.cos((t1 - t0) * 10) * 0.25 + 0.75),
                                        255 * (math.cos((t1 - t0) * 10) * 0.25 + 0.75),
                                        255 * (math.cos((t1 - t0) * 10) * 0.25 + 0.75)))
        rect = string.get_rect()
        rect.bottomright = pos.bottomright
        screen.blit(string, rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                draw_map(game.map.array[item.position[0]], divmod(int((t1 - t0) * 3), 4)[1])
                return


def draw_detector_info():
    pass


def draw_shop_welcome(warrior):
    global TIME_FLAG, t0
    pos = pygame.rect.Rect((0, 0), (6 * 32 + 16, 6 * 32 + 16))
    pos.center = (11.5 * 32, 6.5 * 32 + 5)
    while True:
        t1 = time.process_time()
        delta_t = divmod(int((t1 - t0) * 3), 4)[1]
        if TIME_FLAG != delta_t:
            TIME_FLAG = delta_t
            draw_map(warrior.game.map.array[warrior.position[0]], TIME_FLAG)
        draw_rectangle_border(pos.topleft, pos.bottomright)
        pygame.draw.rect(screen, (0, 0, 0), pos)
        string = arial_font[10].render('-- Space --', True,
                                       (255 * (math.cos((t1 - t0) * 10) * 0.5 + 0.5),
                                        255 * (math.cos((t1 - t0) * 10) * 0.5 + 0.5),
                                        255 * (math.cos((t1 - t0) * 10) * 0.5 + 0.5)))
        rect = string.get_rect()
        rect.bottomright = pos.bottomright
        screen.blit(string, rect)
        screen.blit(img_list['Shop'].subsurface((delta_t * 32, 0), (32, 32)),
                    (pos.left + 5, pos.top + 5))
        print_string(u'商  店  老  板', 18, (pos.left + 44, pos.top + 8))
        welcome = [u'    嗨，你好，英雄的勇士，这里',
                   u'是怪物商店，这里告诉你一些操',
                   u'作方法：',
                   u'    使用小键盘上的 8 和 2 可以',
                   u'在菜单中进行选择，使用小键盘',
                   u'上的 5 或是 Space 键可以用来',
                   u'确认你的选择！',
                   u'    同时，在商人或神秘老人处进',
                   u'行交易也是一样的操作方法！',
                   u'    知道了吗？勇士！']
        for i in range(len(welcome)):
            print_string(welcome[i], 14, (pos.left + 5, pos.top + 40 + i * 16))
        pygame.display.update()
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                draw_map(warrior.game.map.array[warrior.position[0]], divmod(int((t1 - t0) * 3), 4)[1])
                return


def draw_shop_interface(warrior, price, buff):
    global TIME_FLAG, t0
    pos = pygame.rect.Rect((0, 0), (6 * 32 + 16, 6 * 32 + 16))
    pos.center = (11.5 * 32, 6.5 * 32 + 5)
    highlight = 0
    while True:
        t1 = time.process_time()
        delta_t = divmod(int((t1 - t0) * 3), 4)[1]
        if TIME_FLAG != delta_t:
            TIME_FLAG = delta_t
            draw_map(warrior.game.map.array[warrior.position[0]], TIME_FLAG)
            draw_info(warrior.game)
        draw_rectangle_border(pos.topleft, pos.bottomright)
        pygame.draw.rect(screen, (0, 0, 0), pos)
        screen.blit(img_list['Shop'].subsurface((delta_t * 32, 0), (32, 32)),
                    (pos.left + 5, pos.top + 5))
        message = [u'    想要增加你的能力吗？',
                   u'如果你有 ' + str(price) + ' 个金币，你',
                   u'可以任意选择一项：']
        for i in range(len(message)):
            print_string(message[i], 14, (pos.left + 44, pos.top + 5 + 14 * i))
        goods = [u'增加 ' + str(buff[0]) + u' 点生命',
                 u'增加 ' + str(buff[1]) + u' 点攻击',
                 u'增加 ' + str(buff[2]) + u' 点防御',
                 u'离开商店']
        for i in range(len(goods)):
            print_string(goods[i], 16, center=(11.5 * 32, 6 * 32 - 8 + i * 32))
        rect = pygame.rect.Rect((8.5 * 32, (5 + highlight) * 32 + 8), (6 * 32, 32))
        map_border = [(rect.left - 2, rect.top - 2),
                      (rect.right, rect.top - 2),
                      (rect.right, rect.bottom),
                      (rect.left - 2, rect.bottom)]
        color = 255 * (math.cos((t1 - t0) * 10) * 0.25 + 0.75)
        pygame.draw.lines(screen, (color, color, color), True, map_border, 3)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_5:
                    if highlight == 3:
                        return
                    elif warrior.gold >= price:
                        warrior.gold -= price
                        if highlight == 0:
                            warrior.hp += buff[0]
                        elif highlight == 1:
                            warrior.attack += buff[1]
                        elif highlight == 2:
                            warrior.defense += buff[2]
                        warrior.game.indicator['first_use_shop'] = True
                        break
                elif event.key == pygame.K_2:
                    highlight = min(3, highlight + 1)
                elif event.key == pygame.K_8:
                    highlight = max(0, highlight - 1)


def draw_expshop_interface(warrior, price, buff):
    global TIME_FLAG, t0
    pos = pygame.rect.Rect((0, 0), (6 * 32 + 16, 6 * 32 + 16))
    pos.center = (11.5 * 32, 6.5 * 32 + 5)
    highlight = 0
    while True:
        t1 = time.process_time()
        delta_t = divmod(int((t1 - t0) * 3), 4)[1]
        if TIME_FLAG != delta_t:
            TIME_FLAG = delta_t
            draw_map(warrior.game.map.array[warrior.position[0]], TIME_FLAG)
            draw_info(warrior.game)
        draw_rectangle_border(pos.topleft, pos.bottomright)
        pygame.draw.rect(screen, (0, 0, 0), pos)
        screen.blit(img_list['Elder'].subsurface((delta_t * 32, 0), (32, 32)),
                    (pos.left + 5, pos.top + 5))
        message = [u'    你好，英雄的人类，只',
                   u'要你有足够的经验，我就',
                   u'可以让你变得更强大：']
        for i in range(len(message)):
            print_string(message[i], 14, (pos.left + 44, pos.top + 5 + 14 * i))
        goods = [u'提升 ' + str(buff[0]) + u' 级 (需要 ' + str(price[0]) + u' 点)',
                 u'增加攻击 ' + str(buff[1]) + u' (需要' + str(price[1]) + u' 点)',
                 u'增加防御 ' + str(buff[2]) + u' (需要' + str(price[2]) + u' 点)',
                 u'离开商店']
        for i in range(len(goods)):
            print_string(goods[i], 16, center=(11.5 * 32, 6 * 32 - 8 + i * 32))
        rect = pygame.rect.Rect((8.5 * 32, (5 + highlight) * 32 + 8), (6 * 32, 32))
        map_border = [(rect.left - 2, rect.top - 2),
                      (rect.right, rect.top - 2),
                      (rect.right, rect.bottom),
                      (rect.left - 2, rect.bottom)]
        color = 255 * (math.cos((t1 - t0) * 10) * 0.25 + 0.75)
        pygame.draw.lines(screen, (color, color, color), True, map_border, 3)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_5:
                    if highlight == 3:
                        return
                    elif warrior.exp >= price[highlight]:
                        warrior.exp -= price[highlight]
                        if highlight == 0:
                            warrior.level += buff[0]
                            warrior.hp += buff[0] * 1000
                            warrior.attack += buff[0] * 10
                            warrior.defense += buff[0] * 10
                        elif highlight == 1:
                            warrior.attack += buff[1]
                        elif highlight == 2:
                            warrior.defense += buff[2]
                        break
                elif event.key == pygame.K_2:
                    highlight = min(3, highlight + 1)
                elif event.key == pygame.K_8:
                    highlight = max(0, highlight - 1)


def draw_keyshop_interface(warrior, price, buff):
    global TIME_FLAG, t0
    pos = pygame.rect.Rect((0, 0), (6 * 32 + 16, 6 * 32 + 16))
    pos.center = (11.5 * 32, 6.5 * 32 + 5)
    highlight = 0
    while True:
        t1 = time.process_time()
        delta_t = divmod(int((t1 - t0) * 3), 4)[1]
        if TIME_FLAG != delta_t:
            TIME_FLAG = delta_t
            draw_map(warrior.game.map.array[warrior.position[0]], TIME_FLAG)
            draw_info(warrior.game)
        draw_rectangle_border(pos.topleft, pos.bottomright)
        pygame.draw.rect(screen, (0, 0, 0), pos)
        screen.blit(img_list['Merchant'].subsurface((delta_t * 32, 0), (32, 32)),
                    (pos.left + 5, pos.top + 5))
        message = [u'    相信你一定有特殊的需',
                   u'要，只要你有金币，我就',
                   u'可以帮你：']
        for i in range(len(message)):
            print_string(message[i], 14, (pos.left + 44, pos.top + 5 + 14 * i))
        goods = [u'购买 ' + str(buff[0]) + u' 把黄钥匙 ($ ' + str(price[0]) + u' )',
                 u'购买 ' + str(buff[1]) + u' 把蓝钥匙 ($ ' + str(price[1]) + u' )',
                 u'购买 ' + str(buff[2]) + u' 把红钥匙 ($ ' + str(price[2]) + u' )',
                 u'离开商店']
        for i in range(len(goods)):
            print_string(goods[i], 16, center=(11.5 * 32, 6 * 32 - 8 + i * 32))
        rect = pygame.rect.Rect((8.5 * 32, (5 + highlight) * 32 + 8), (6 * 32, 32))
        map_border = [(rect.left - 2, rect.top - 2),
                      (rect.right, rect.top - 2),
                      (rect.right, rect.bottom),
                      (rect.left - 2, rect.bottom)]
        color = 255 * (math.cos((t1 - t0) * 10) * 0.25 + 0.75)
        pygame.draw.lines(screen, (color, color, color), True, map_border, 3)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE or event.key == pygame.K_5:
                    if highlight == 3:
                        return
                    elif warrior.gold >= price[highlight]:
                        warrior.gold -= price[highlight]
                        warrior.keys[highlight] += 1
                        break
                elif event.key == pygame.K_2:
                    highlight = min(3, highlight + 1)
                elif event.key == pygame.K_8:
                    highlight = max(0, highlight - 1)




