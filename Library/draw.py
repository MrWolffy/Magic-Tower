# -*- coding: utf-8 -*-
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


def print_string(string, fontsize, topleft=(0, 0), center=None, bottomright=None, color=(255, 255, 255)):
    info = arial_font[fontsize].render(string, True, color)
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
    # 先画地图和信息
    draw_map(game)
    draw_info(game)
    # 逐个判断有没有mask，有的话就叠到原有界面上
    if game.status["instruction"]["display"]:
        draw_instruction(game)
    elif game.status["dialog"]["display"]:
        draw_dialog(game)
    elif game.status["shop"]["display"]:
        draw_shop(game)
    elif game.status["detector"]["display"]:
        draw_detector(game)
    elif game.status["aircraft"]["display"]:
        draw_aircraft(game)
    elif game.status["alert"]["display"]:
        draw_alert(game)
    elif game.status["fight"]["display"]:
        draw_fight(game)
    pygame.display.update()


def init_interface(game):
    global screen
    screen = pygame.display.set_mode(((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 10), 0, 32)
    screen.fill((0, 0, 0))
    for i in range(1, 33):
        arial_font.append(pygame.font.Font('Library/Arial.ttf', i))
    arial_font.append(pygame.font.Font('Library/Arial.ttf', 64))


def draw_map(game):
    level = game.map.array[game.warrior.position[0]]
    # 画整体大背景
    bg = pygame.image.load('UI/Background.png')
    fill_rectangle((0, 5), ((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 5), bg)
    # 画地图背景（用Floor当作地图背景）
    width = len(level[0])
    height = len(level)
    fill_rectangle((6 * 32, 32 + 5), ((width + 6) * 32, ((height + 1) * 32 + 5)), img_list['Floor'])
    draw_rectangle_border((6 * 32, 32 + 5), ((game.map.width + 6) * 32, (game.map.height + 1) * 32 + 5))
    # 逐个格画物体
    for i in range(width):
        for j in range(height):
            temp_type = type(level[j][i])
            if temp_type.__name__ != 'Floor':
                # 门有开门动作
                if issubclass(temp_type, Door):
                    if game.status['door_open']['display'] and \
                            j == game.status['door_open']['position'][1] and \
                            i == game.status['door_open']['position'][2]:
                        y_offset = game.status['door_open']['frame']
                        screen.blit(img_list[temp_type.__name__].subsurface((0, 32 * 2 * y_offset), (32, 32)),
                                    ((i + 6) * 32, (j + 1) * 32 + 5))
                    else:
                        screen.blit(img_list[temp_type.__name__].subsurface((0, 0), (32, 32)),
                                    ((i + 6) * 32, (j + 1) * 32 + 5))
                # 勇士有朝向问题
                elif temp_type == Warrior:
                    x_offset = {0: 0, 1: 1, 2: 3, 3: 2}[int(game.status['walk']['frame'] / 2)]
                    y_offset = {'down': 0, 'left': 1, 'right': 2, 'up': 3}[level[j][i].toward]
                    screen.blit(img_list['Warrior'].subsurface((32 * x_offset, 33 * y_offset), (32, 32)),
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
    # 勇士头像
    print_string(str(frame % 24), 10, (32, 32 + 5))
    warrior_image = img_list['Warrior'].subsurface((0, 0), (32, 32))
    screen.blit(pygame.transform.scale(warrior_image, (40, 40)), (40, 40))
    # 等级
    print_string(str(warrior.level), 32, (3 * 32, 44))
    print_string(u'级', 16, (4 * 32 + 8, 62))
    # 基本信息
    info = [u'生命', u'攻击', u'防御', u'金币', u'经验']
    for i in range(len(info)):
        print_string(info[i], 16, (32 + 6, 2 * 32 + 28 + i * 20))
    print_string(str(warrior.hp), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 0 * 20))
    print_string(str(warrior.attack), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 1 * 20))
    print_string(str(warrior.defense), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 2 * 20))
    print_string(str(warrior.gold), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 3 * 20))
    print_string(str(warrior.exp), 16, center=(3.5 * 32 + 4, 3 * 32 + 8 + 4 * 20))

    # second
    # 钥匙图片
    key_image = img_list['YellowKey']
    screen.blit(key_image, (32 + 4, 6 * 32 + 5 + 8))
    key_image = img_list['BlueKey']
    screen.blit(key_image, (32 + 4, 7 * 32 + 5 + 8))
    key_image = img_list['RedKey']
    screen.blit(key_image, (32 + 4, 8 * 32 + 5 + 8))
    # 钥匙数量
    print_string(str(warrior.keys[0]), 22, bottomright=(4 * 32, 7 * 32 + 5 + 6))
    print_string(str(warrior.keys[1]), 22, bottomright=(4 * 32, 8 * 32 + 5 + 6))
    print_string(str(warrior.keys[2]), 22, bottomright=(4 * 32, 9 * 32 + 5 + 6))
    # 单位"个"
    info = arial_font[16].render(u'个', True, (255, 255, 255))
    screen.blit(info, (4 * 32 + 12, 6 * 32 + 18))
    screen.blit(info, (4 * 32 + 12, 7 * 32 + 18))
    screen.blit(info, (4 * 32 + 12, 8 * 32 + 18))

    # third
    # 当前层数
    level = warrior.position[0]
    if level == 0:
        print_string(u'序  章', 16, center=(3 * 32, 9.5 * 32 + 5 + 8))
    else:
        print_string(u'第 ' + str(level) + u' 层', 16, center=(3 * 32, 9.5 * 32 + 5 + 8))

    # forth
    # 指令
    print_string(u'S 保存   Q 退出程序', 14, (32 + 2, 11 * 32 - 6))
    print_string(u'A 读取   R 重新开始', 14, (32 + 2, 12 * 32 - 16))


def draw_instruction(game):
    instruction = game.status["instruction"]

    # 画矩形和边框
    pos = pygame.rect.Rect((5 * 32, 5 * 32), (12 * 32 + 24, 4 * 32))
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (0, 0, 0), pos)

    # 名字
    string = ' '.join(instruction["name"])
    print_string(string, 24, center=(pos.centerx, 6 * 32 - 8))

    # 内容
    message = instruction["content"]
    for i in range(len(message)):
        print_string(message[i], 16, (pos.left + 4, pos.top + 48 + 20 * i))

    # 右下角的Space
    color = 255 * (math.cos(frame / 3) * 0.25 + 0.75)
    string = arial_font[10].render('-- Space --', True, (color, color, color))
    rect = string.get_rect()
    rect.bottomright = pos.bottomright
    screen.blit(string, rect)


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
    # 不同种类商店的格式过于复杂，所以拆成多个函数
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
    pygame.draw.lines(screen, (color, color, color), True, map_border, 2)


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
    pygame.draw.lines(screen, (color, color, color), True, map_border, 2)


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
    pygame.draw.lines(screen, (color, color, color), True, map_border, 2)


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
    pygame.draw.lines(screen, (color, color, color), True, map_border, 2)


def draw_detector(game):
    # 获取怪物种类
    map = game.map.array[game.warrior.position[0]]
    monsters = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            obj_type = type(map[i][j])
            if issubclass(obj_type, Monster) and obj_type.__name__ not in monsters:
                monsters.append(obj_type.__name__)
    # 没有怪物就不展示
    if len(monsters) == 0:
        return
    # 背景涂黑
    rect = pygame.rect.Rect((6 * 32, 32 + 5), (11 * 32, 11 * 32))
    pygame.draw.rect(screen, (0, 0, 0), rect)
    # 依次画怪物信息
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
    print_string(
        str(game.info['creature_info'][monster]['gold']) + u' · ' + str(game.info['creature_info'][monster]['exp']),
        14, center=(16 * 32 - 8, 52 + 40 * position))
    print_string(str(damage), 14, center=(16 * 32 - 8, 68 + 40 * position))


def draw_aircraft(game):
    if game.status["aircraft"]["welcome"]:
        draw_aircraft_welcome(game)
    else:
        draw_aircraft_selection(game)


def draw_aircraft_welcome(game):
    # 画矩形和边框
    pos = pygame.rect.Rect((7 * 32, 2 * 32), (9 * 32, 9 * 32))
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (0, 0, 0), pos)

    # 标题
    string = ' '.join("楼层跳跃")
    print_string(string, 32, center=(pos.centerx, 3 * 32))

    # 指导语
    message = ["    本功能可以使您快速地在已经走",
               "过的各个楼层间进行快速转换。",
               "    其具体操作方法为：",
               "    8 键  代表光标上移一格",
               "    2 键  代表光标下移一格",
               "    Space 或 5 键代表确认选择",
               "    本功能只允许在已经走过的楼层",
               "间进行转换，如果该楼层还没有走",
               "过，那么将无法转换到位置。"]
    for i in range(len(message)):
        print_string(message[i], 18, (pos.left + 8, pos.top + 64 + 20 * i))

    # 右下角的Space
    color = 255 * (math.cos(frame / 3) * 0.25 + 0.75)
    string = arial_font[10].render('-- Space --', True, (color, color, color))
    rect = string.get_rect()
    rect.bottomright = pos.bottomright
    screen.blit(string, rect)


def draw_aircraft_selection(game):
    # 画矩形和边框
    pos = pygame.rect.Rect((7 * 32, 2 * 32), (9 * 32, 9 * 32))
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (0, 0, 0), pos)

    # 标题
    string = ' '.join("楼层跳跃")
    print_string(string, 32, center=(pos.centerx, 3 * 32))

    # 选项
    for i in range(1, 21):
        message = "第 " + str(i) + " 层"
        x_offset, y_offset = divmod(i - 1, 7)
        print_string(message, 18,
                     center=(pos.left + 48 + 3 * 32 * x_offset, pos.top + 30 * (y_offset + 2.5)))

    # 高亮框
    x_offset, y_offset = divmod(game.status["aircraft"]["highlight"], 7)
    rect = pygame.rect.Rect((0, 0), (3 * 32 - 8, 24))
    rect.center = (pos.left + 48 + 3 * 32 * x_offset, pos.top + 30 * (y_offset + 2.5))
    map_border = [(rect.left - 2, rect.top - 2),
                  (rect.right, rect.top - 2),
                  (rect.right, rect.bottom),
                  (rect.left - 2, rect.bottom)]
    color = 255 * (math.cos(frame / 3) * 0.25 + 0.75)
    pygame.draw.lines(screen, (color, color, color), True, map_border, 2)

    # 右下角的Space
    string = arial_font[10].render('-- Space --', True, (color, color, color))
    rect = string.get_rect()
    rect.bottomright = pos.bottomright
    screen.blit(string, rect)


def draw_alert(game):
    alert = game.status["alert"]

    # 画矩形和边框
    pos = pygame.rect.Rect((8, 4 * 32), ((game.map.width + 7) * 32 - 16, 2 * 32))
    draw_rectangle_border(pos.topleft, pos.bottomright)
    fill_rectangle(pos.topleft, pos.bottomright, pygame.image.load('UI/Floor.png'))

    # 写字
    print_string(alert["content"], 32, center=pos.center)


def draw_fight(game):
    fight = game.status["fight"]

    # 画矩形和边框
    pos = pygame.rect.Rect((8, 32), ((game.map.width + 7) * 32 - 16, 7 * 32))
    draw_rectangle_border(pos.topleft, pos.bottomright)
    fill_rectangle(pos.topleft, pos.bottomright, pygame.image.load('UI/Floor.png'))

    # "vs"
    print_string("VS", 32, center=pos.center)

    # 怪的信息
    # 头像
    pos = pygame.rect.Rect((16, 2 * 32 - 8), (3 * 32, 3 * 32))
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (85, 85, 85), pos)
    image = img_list['Floor'].subsurface((0, 0), (32, 32))
    screen.blit(pygame.transform.scale(image, (64, 64)), (32, 2 * 32 + 8))
    image = img_list[fight['monster']['name']].subsurface((int(frame / 8) % 4 * 32, 0), (32, 32))
    screen.blit(pygame.transform.scale(image, (64, 64)), (32, 2 * 32 + 8))
    # "怪物"二字
    print_string("怪物", 24, center=(2 * 32, 6 * 32))
    # 生命值
    point = (pos.right + 8, pos.top)
    print_string("生命值：", 16, point)
    point = (point[0], point[1] + 24)
    pygame.draw.line(screen, (255, 255, 255), point, (point[0] + 3 * 32, point[1]), 2)
    print_string(str(fight['monster']['hp']), 20, bottomright=(point[0] + 3 * 32, point[1] + 32))
    # 攻击力
    point = (point[0], point[1] + 32)
    print_string("攻击力：", 16, point)
    point = (point[0], point[1] + 24)
    pygame.draw.line(screen, (255, 255, 255), point, (point[0] + 3 * 32, point[1]), 2)
    print_string(str(fight['monster']['attack']), 20, bottomright=(point[0] + 3 * 32, point[1] + 32))
    # 防御力
    point = (point[0], point[1] + 32)
    print_string("防御力：", 16, point)
    point = (point[0], point[1] + 24)
    pygame.draw.line(screen, (255, 255, 255), point, (point[0] + 3 * 32, point[1]), 2)
    print_string(str(fight['monster']['defense']), 20, bottomright=(point[0] + 3 * 32, point[1] + 32))

    # 勇士的信息
    # 头像
    pos = pygame.rect.Rect(((game.map.width + 3) * 32 + 8, 2 * 32 - 8), (3 * 32, 3 * 32))
    draw_rectangle_border(pos.topleft, pos.bottomright)
    pygame.draw.rect(screen, (85, 85, 85), pos)
    image = img_list['Warrior'].subsurface((0, 0), (32, 32))
    screen.blit(pygame.transform.scale(image, (64, 64)), ((game.map.width + 3) * 32 + 24, 2 * 32 + 8))
    # "勇士"二字
    print_string("勇士", 24, center=((game.map.width + 4.5) * 32 + 4, 6 * 32))
    # 生命值
    point = (pos.left - 3 * 32 - 8, pos.top)
    print_string("：生命值", 16, bottomright=(point[0] + 3 * 32, point[1] + 22))
    point = (point[0], point[1] + 24)
    pygame.draw.line(screen, (255, 255, 255), point, (point[0] + 3 * 32, point[1]), 2)
    print_string(str(fight['warrior']['hp']), 20, (point[0], point[1] + 4))
    # 攻击力
    point = (point[0], point[1] + 32)
    print_string("：攻击力", 16, bottomright=(point[0] + 3 * 32, point[1] + 22))
    point = (point[0], point[1] + 24)
    pygame.draw.line(screen, (255, 255, 255), point, (point[0] + 3 * 32, point[1]), 2)
    print_string(str(game.warrior.attack), 20, (point[0], point[1] + 4))
    # 防御力
    point = (point[0], point[1] + 32)
    print_string("：防御力", 16, bottomright=(point[0] + 3 * 32, point[1] + 22))
    point = (point[0], point[1] + 24)
    pygame.draw.line(screen, (255, 255, 255), point, (point[0] + 3 * 32, point[1]), 2)
    print_string(str(game.warrior.defense), 20, (point[0], point[1] + 4))


def draw_begin():
    message = ["    这是一个很古老的故事",
               "    在很久很久以前，在遥远的西方大地上，有",
               "着这样一个王国，王国虽小但全国的人民都生",
               "活的非常幸福和快乐。",
               "    突然有一天，从天空飞来一群可怕的怪物，",
               "它们来到皇宫，抢走了国王唯一的女儿。",
               "    第二天，国王便向全国下达了紧急令，只要",
               "谁能将公主给找回来，他便将王位让给他。",
               "    于是，全国的勇士都出发了。他们的足迹",
               "走遍了全国的各个角落，可一点儿线索都没有",
               "找到，时间很快过去了一个月。",
               "    终于，在国王下达命令的第三十一天，一个",
               "从远方归来的人告诉国王，说在海边的一座小",
               "岛上，曾看到一群怪物出现过。",
               "    勇士们又出发了，可是，却没有一个人可以",
               "回来，有幸回来的，都再也不敢去了。",
               "    而我们的故事，便是从这里开始……"]
    t0 = time.process_time()
    # 开始界面持续的帧数为700，试验得到
    time_flag = 0
    while time_flag < 700:
        t1 = time.process_time()
        if int((t1 - t0) * 24) != time_flag:
            time_flag = int((t1 - t0) * 24)
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
            # 滚动字
            for i in range(len(message)):
                print_string(message[i], 24, (50, 30 * (i + 10) - time_flag))

            # 右下角的Space
            color = 255 * (math.cos(time_flag / 3) * 0.25 + 0.75)
            string = arial_font[10].render('-- Space --', True, (color, color, color))
            rect = string.get_rect()
            rect.bottomright = ((game.map.width + 7) * 32, (game.map.height + 2) * 32 + 10)
            screen.blit(string, rect)
            pygame.display.update()
    # 结束
    screen.fill((0, 0, 0))


def draw_end():
    message = ["    大魔头被杀死了，公主也被救出了塔，蝶仙",
               "的精力也恢复了。",
               "    当勇士和公主一起走出塔来的时候，国王也",
               "带着军队来到了岛外。",
               "    一切都是那么的平常。",
               "    回国后，国王为勇士和公主举行了隆重而且",
               "盛大的婚礼，并且宣布由勇士继承国王的位",
               "置。从此以后，勇士和公主就幸福的生活在一",
               "起了。"]
    t0 = time.process_time()
    time_flag = 0
    # 结束语
    while time_flag < 700:
        t1 = time.process_time()
        if int((t1 - t0) * 24) != time_flag:
            time_flag = int((t1 - t0) * 24)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            screen.fill((0, 0, 0))
            # 滚动字
            for i in range(len(message)):
                print_string(message[i], 24, (50, 30 * (i + 15) - time_flag))
            pygame.display.update()
    # "终"字
    t0 = time.process_time()
    time_flag = 0
    while time_flag < 300:
        t1 = time.process_time()
        if int((t1 - t0) * 24) != time_flag:
            time_flag = int((t1 - t0) * 24)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            screen.fill((0, 0, 0))
            # 字
            color = 255 * (-math.cos(time_flag / 48) * 0.5 + 0.5)
            string = arial_font[33].render('终', True, (color, color, color))
            rect = string.get_rect()
            rect.center = ((game.map.width + 7) * 16, (game.map.height + 2) * 16 + 5)
            screen.blit(string, rect)
            string = arial_font[32].render('The End', True, (color, color, color))
            rect = string.get_rect()
            rect.center = ((game.map.width + 7) * 16, (game.map.height + 5) * 16 + 5)
            screen.blit(string, rect)
            pygame.display.update()
