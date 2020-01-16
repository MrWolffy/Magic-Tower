# -*- coding: utf-8 -*-
import os
import pygame
from Library.items import *


def read_image():
    imglist = {}
    dirlist = os.listdir('UI')
    for dir in dirlist:
        if dir.endswith('.png'):
            imglist[dir[:-4]] = pygame.image.load('UI/' + dir)
    return imglist


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


def print_string(string, fontsize, topleft=(0, 0), center=None, bottomright=None):
    info = arial_font[fontsize].render(string, True, (255, 255, 255))
    if center is not None:
        info_rect = info.get_rect()
        info_rect.center = center
        screen.blit(info, info_rect)
    elif bottomright is not None:
        info_rect = info.get_rect()
        info_rect.bottomright = bottomright
        screen.blit(info, info_rect)
    else:
        screen.blit(info, topleft)


arial_font = [None]
screen = None
img_list = read_image()
frame = 0


def draw(game, ts):
    global frame
    frame = ts
    draw_map(game.map.array[game.warrior.position[0]])
    draw_info(game)
    if game.status["dialog"]["display"]:
        draw_dialog(game)
    elif game.status["shop"]["display"]:
        draw_shop(game)
    elif game.status["detector"]["display"]:
        draw_detector(game)
    pygame.display.update()


def init_interface(game):
    global screen
    screen = pygame.display.set_mode(((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 10), 0, 32)
    screen.fill((0, 0, 0))
    bg = pygame.image.load('UI/Background.png')
    for i in range(1, 33):
        arial_font.append(pygame.font.Font('Library/Arial.ttf', i))
    fill_rectangle((0, 5), ((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 5), bg)
    draw_rectangle_border((6 * 32, 32 + 5), ((game.map.width + 6) * 32, (game.map.height + 1) * 32 + 5))


def draw_map(level):
    width = len(level[0])
    height = len(level)
    fill_rectangle((6 * 32, 32 + 5), ((width + 6) * 32, ((height + 1) * 32 + 5)), img_list['Floor'])
    for i in range(width):
        for j in range(height):
            temp_type = type(level[j][i])
            if temp_type.__name__ != 'Floor':
                # 有保留动作的
                if issubclass(temp_type, (Door, Warrior)):
                    screen.blit(img_list[temp_type.__name__].subsurface((0, 0), (32, 32)),
                                ((i + 6) * 32, (j + 1) * 32 + 5))
                # 能动的
                elif issubclass(temp_type, (Creature, Lava, Star)):
                    screen.blit(img_list[temp_type.__name__].subsurface((int(frame / 8) % 4 * 32, 0), (32, 32)),
                                ((i + 6) * 32, (j + 1) * 32 + 5))
                # 不能动的
                else:
                    screen.blit(img_list[temp_type.__name__], ((i + 6) * 32, (j + 1) * 32 + 5))


def draw_info(game):
    draw_info_background()
    draw_info_content(game.warrior)


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


def draw_info_content(warrior):
    # first
    print_string(str(frame % 24), 10, (32, 32 + 5))
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


def draw_dialog(game):
    dialog = game.status["dialog"]
    item = dialog["talking"]

    # 画矩形和边框
    if item == 'Warrior':
        pos = pygame.rect.Rect((8 * 32, 8 * 32), (7 * 32, 2 * 32 + 8))
    else:
        pos = pygame.rect.Rect((7 * 32, 5 * 32), (7 * 32, 2 * 32 + 8))
    content = dialog["content"].split('\t')
    draw_rectangle_border(pos.topleft, pos.bottomright)
    fill_rectangle(pos.topleft, pos.bottomright, pygame.image.load('UI/Floor.png'))

    # 说话人
    print_string(game.info['creature_info'][item]['chinese_name'] + ':',
                 16, (pos.left + 48, pos.top + 5))

    # 说的话
    for i in range(len(content)):
        print_string(content[i], 14, (pos.left + 48, pos.top + 24 + 14 * i))

    # 头像
    if item != 'Warrior':
        screen.blit(img_list['Floor'], (pos.left + 5, pos.top + 5))
        screen.blit(img_list[item].subsurface((int(frame / 8) % 4 * 32, 0), (32, 32)),
                    (pos.left + 5, pos.top + 5))
    else:
        screen.blit(img_list[item].subsurface((0, 0), (32, 32)),
                    (pos.left + 5, pos.top + 5))

    # 右下角的Space
    color = 255 * (math.cos(frame / 3) * 0.25 + 0.75)
    string = arial_font[10].render('-- Space --', True, (color, color, color))
    rect = string.get_rect()
    rect.bottomright = pos.bottomright
    screen.blit(string, rect)


def draw_shop(game):
    if game.status["shop"]["first_use"]:
        draw_shop_welcome()
    elif game.status["shop"]["type"] == 'gold':
        draw_shop_interface(game)
    elif game.status["shop"]["type"] == 'exp':
        draw_expshop_interface(game)
    elif game.status["shop"]["type"] == 'key':
        draw_keyshop_interface(game)
    elif game.status["shop"]["type"] == 'key_sell':
        draw_keyshop_sell_interface(game)


def draw_shop_welcome():
    # 画矩形和边框
    pos = pygame.rect.Rect((0, 0), (6 * 32 + 16, 6 * 32 + 16))
    pos.center = (11.5 * 32, 6.5 * 32 + 5)
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (0, 0, 0), pos)

    # 头像和npc名
    screen.blit(img_list['Shop'].subsurface((int(frame / 8) % 4 * 32, 0), (32, 32)),
                (pos.left + 5, pos.top + 5))

    print_string(u'商  店  老  板', 18, (pos.left + 44, pos.top + 8))

    # 指导语
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

    # 右下角的space
    color = 255 * (math.cos(frame / 3) * 0.25 + 0.75)
    string = arial_font[10].render('-- Space --', True, (color, color, color))
    rect = string.get_rect()
    rect.bottomright = pos.bottomright
    screen.blit(string, rect)


def draw_shop_interface(game):
    shop = game.status["shop"]

    # 画矩形和边框
    pos = pygame.rect.Rect((0, 0), (6 * 32 + 16, 6 * 32 + 16))
    pos.center = (11.5 * 32, 6.5 * 32 + 5)
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (0, 0, 0), pos)

    # 头像
    screen.blit(img_list['Shop'].subsurface((int(frame / 8) % 4 * 32, 0), (32, 32)),
                (pos.left + 5, pos.top + 5))

    # 指导语
    message = [u'    想要增加你的能力吗？',
               u'如果你有 ' + str(shop["price"]) + ' 个金币，你',
               u'可以任意选择一项：']
    for i in range(len(message)):
        print_string(message[i], 14, (pos.left + 44, pos.top + 5 + 14 * i))

    # 商品名
    goods = [u'增加 ' + str(shop["buff"][0]) + u' 点生命',
             u'增加 ' + str(shop["buff"][1]) + u' 点攻击',
             u'增加 ' + str(shop["buff"][2]) + u' 点防御',
             u'离开商店']
    for i in range(len(goods)):
        print_string(goods[i], 16, center=(11.5 * 32, 6 * 32 - 8 + i * 32))

    # 高亮
    rect = pygame.rect.Rect((8.5 * 32, (5 + shop["highlight"]) * 32 + 8), (6 * 32, 32))
    map_border = [(rect.left - 2, rect.top - 2),
                  (rect.right, rect.top - 2),
                  (rect.right, rect.bottom),
                  (rect.left - 2, rect.bottom)]
    color = 255 * (math.cos(frame / 3) * 0.25 + 0.75)
    pygame.draw.lines(screen, (color, color, color), True, map_border, 3)


def draw_expshop_interface(game):
    shop = game.status["shop"]

    # 画矩形和边框
    pos = pygame.rect.Rect((0, 0), (6 * 32 + 16, 6 * 32 + 16))
    pos.center = (11.5 * 32, 6.5 * 32 + 5)
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (0, 0, 0), pos)

    # 头像
    screen.blit(img_list['Elder'].subsurface((int(frame / 8) % 4 * 32, 0), (32, 32)),
                (pos.left + 5, pos.top + 5))

    # 指导语
    message = [u'    你好，英雄的人类，只',
               u'要你有足够的经验，我就',
               u'可以让你变得更强大：']
    for i in range(len(message)):
        print_string(message[i], 14, (pos.left + 44, pos.top + 5 + 14 * i))

    # 商品名
    goods = [u'提升 ' + str(shop["buff"][0]) + u' 级 (需要 ' + str(shop["price"][0]) + u' 点)',
             u'增加攻击 ' + str(shop["buff"][1]) + u' (需要' + str(shop["price"][1]) + u' 点)',
             u'增加防御 ' + str(shop["buff"][2]) + u' (需要' + str(shop["price"][2]) + u' 点)',
             u'离开商店']
    for i in range(len(goods)):
        print_string(goods[i], 16, center=(11.5 * 32, 6 * 32 - 8 + i * 32))

    # 高亮
    rect = pygame.rect.Rect((8.5 * 32, (5 + shop["highlight"]) * 32 + 8), (6 * 32, 32))
    map_border = [(rect.left - 2, rect.top - 2),
                  (rect.right, rect.top - 2),
                  (rect.right, rect.bottom),
                  (rect.left - 2, rect.bottom)]
    color = 255 * (math.cos(frame / 3) * 0.25 + 0.75)
    pygame.draw.lines(screen, (color, color, color), True, map_border, 3)


def draw_keyshop_interface(game):
    shop = game.status["shop"]

    # 画矩形和边框
    pos = pygame.rect.Rect((0, 0), (6 * 32 + 16, 6 * 32 + 16))
    pos.center = (11.5 * 32, 6.5 * 32 + 5)
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (0, 0, 0), pos)

    # 头像
    screen.blit(img_list['Merchant'].subsurface((int(frame / 8) % 4 * 32, 0), (32, 32)),
                (pos.left + 5, pos.top + 5))

    # 指导语
    message = [u'    相信你一定有特殊的需',
               u'要，只要你有金币，我就',
               u'可以帮你：']
    for i in range(len(message)):
        print_string(message[i], 14, (pos.left + 44, pos.top + 5 + 14 * i))

    # 商品名
    goods = [u'购买 ' + str(shop["buff"][0]) + u' 把黄钥匙 ($ ' + str(shop["price"][0]) + u' )',
             u'购买 ' + str(shop["buff"][1]) + u' 把蓝钥匙 ($ ' + str(shop["price"][1]) + u' )',
             u'购买 ' + str(shop["buff"][2]) + u' 把红钥匙 ($ ' + str(shop["price"][2]) + u' )',
             u'离开商店']
    for i in range(len(goods)):
        print_string(goods[i], 16, center=(11.5 * 32, 6 * 32 - 8 + i * 32))

    # 高亮
    rect = pygame.rect.Rect((8.5 * 32, (5 + shop["highlight"]) * 32 + 8), (6 * 32, 32))
    map_border = [(rect.left - 2, rect.top - 2),
                  (rect.right, rect.top - 2),
                  (rect.right, rect.bottom),
                  (rect.left - 2, rect.bottom)]
    color = 255 * (math.cos(frame / 3) * 0.25 + 0.75)
    pygame.draw.lines(screen, (color, color, color), True, map_border, 3)


def draw_keyshop_sell_interface(game):
    shop = game.status["shop"]

    # 画矩形和边框
    pos = pygame.rect.Rect((0, 0), (6 * 32 + 16, 6 * 32 + 16))
    pos.center = (11.5 * 32, 6.5 * 32 + 5)
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (0, 0, 0), pos)

    # 头像
    screen.blit(img_list['Merchant'].subsurface((int(frame / 8) % 4 * 32, 0), (32, 32)),
                (pos.left + 5, pos.top + 5))
    # 指导语
    message = [u'    哦，欢迎你的到来，如',
               u'果你手里缺少金币，我可',
               u'以帮你：']
    for i in range(len(message)):
        print_string(message[i], 14, (pos.left + 44, pos.top + 5 + 14 * i))

    # 商品名
    goods = [u'卖出 ' + str(shop["buff"][0]) + u' 把黄钥匙 ($ ' + str(shop["price"][0]) + u' )',
             u'卖出 ' + str(shop["buff"][1]) + u' 把蓝钥匙 ($ ' + str(shop["price"][1]) + u' )',
             u'卖出 ' + str(shop["buff"][2]) + u' 把红钥匙 ($ ' + str(shop["price"][2]) + u' )',
             u'离开商店']
    for i in range(len(goods)):
        print_string(goods[i], 16, center=(11.5 * 32, 6 * 32 - 8 + i * 32))

    # 高亮
    rect = pygame.rect.Rect((8.5 * 32, (5 + shop["highlight"]) * 32 + 8), (6 * 32, 32))
    map_border = [(rect.left - 2, rect.top - 2),
                  (rect.right, rect.top - 2),
                  (rect.right, rect.bottom),
                  (rect.left - 2, rect.bottom)]
    color = 255 * (math.cos(frame / 3) * 0.25 + 0.75)
    pygame.draw.lines(screen, (color, color, color), True, map_border, 3)


def draw_detector(game):
    map = game.map.array[game.warrior.position[0]]
    monsters = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            obj_type = type(map[i][j])
            if issubclass(obj_type, Monster) and obj_type.__name__ not in monsters:
                monsters.append(obj_type.__name__)
    if len(monsters) == 0:
        return
    rect = pygame.rect.Rect((6 * 32, 32 + 5), (11 * 32, 11 * 32))
    pygame.draw.rect(screen, (0, 0, 0), rect)
    for i in range(len(monsters)):
        draw_monster_info(monsters[i], i, int(frame / 8) % 4, game.warrior.can_beat(monsters[i])[1])


def draw_monster_info(monster, position, time_flag, damage):
    # 头像
    screen.blit(img_list['Floor'], (6 * 32 + 8, 44 + 40 * position))
    screen.blit(img_list[monster].subsurface((time_flag * 32, 0), (32, 32)),
                (6 * 32 + 8, 44 + 40 * position))

    # 头像的边框
    rect = pygame.rect.Rect((6 * 32 + 8, 44 + 40 * position), (32, 32))
    map_border = [(rect.left - 1, rect.top - 1),
                  (rect.right, rect.top - 1),
                  (rect.right, rect.bottom),
                  (rect.left - 1, rect.bottom)]
    pygame.draw.lines(screen, (190, 107, 39), True, map_border, 2)

    # 信息
    print_string(u'名称', 14, center=(8 * 32, 52 + 40 * position))
    print_string(u'生命', 14, center=(8 * 32, 68 + 40 * position))
    print_string(game.info['creature_info'][monster]['chinese_name'], 14, center=(9.5 * 32, 52 + 40 * position))
    print_string(str(game.info['creature_info'][monster]['hp']), 14, center=(9.5 * 32, 68 + 40 * position))
    print_string(u'攻击', 14, center=(11 * 32 + 8, 52 + 40 * position))
    print_string(u'防御', 14, center=(11 * 32 + 8, 68 + 40 * position))
    print_string(str(game.info['creature_info'][monster]['attack']), 14, bottomright=(13 * 32, 62 + 40 * position))
    print_string(str(game.info['creature_info'][monster]['defense']), 14, bottomright=(13 * 32, 78 + 40 * position))
    print_string(u'金 · 经', 14, center=(14 * 32, 52 + 40 * position))
    print_string(u'损失', 14, center=(14 * 32, 68 + 40 * position))
    print_string(str(game.info['creature_info'][monster]['gold']) + u' · ' + str(game.info['creature_info'][monster]['exp']),
                 14, center=(16 * 32 - 8, 52 + 40 * position))
    print_string(str(damage), 14, center=(16 * 32 - 8, 68 + 40 * position))


def draw_end():
    pass




