# -*- coding: utf-8 -*-
import Library.items as items
import math


def test_talk(self, warrior):
    def callback():
        warrior.keys[0] += 1
        warrior.keys[1] += 1
        warrior.keys[2] += 1
        items.game.map.array[0][8][5] = items.Floor()
        items.game.map.array[0][8][4] = self
        self.position = [0, 8, 4]
        self.talk_to = fairy_lv0_talk2

    items.game.process_talk([], callback)


def fairy_lv0_talk(self, warrior):
    if items.game.info["indicator"]["fairy_lv0_talk"] == 0:
        items.game.info["indicator"]["fairy_lv0_talk"] = 1
        fairy_lv0_talk1(self, warrior)
    elif items.game.info["indicator"]["fairy_lv0_talk"] == 1:
        items.game.info["indicator"]["fairy_lv0_talk"] = 2
        fairy_lv0_talk2(self, warrior)


def fairy_lv0_talk1(self, warrior):
    def callback():
        warrior.keys[0] += 1
        warrior.keys[1] += 1
        warrior.keys[2] += 1
        items.game.map.array[0][8][5] = items.Floor()
        items.game.map.array[0][8][4] = self
        self.position = [0, 8, 4]

    items.game.process_talk(items.game.info["creature_info"]["Fairy"]["dialog"][0], callback)


def fairy_lv0_talk2(self, warrior):
    def callback():
        items.game.map.array[20][7][5] = items.UpStair()
        warrior.hp = math.floor(warrior.hp * 4 / 3)
        warrior.attack = math.floor(warrior.attack * 4 / 3)
        warrior.defense = math.floor(warrior.defense * 4 / 3)

    if items.game.info['indicator']['warrior_get_cross']:
        items.game.process_talk(items.game.info["creature_info"]["Fairy"]["dialog"][1], callback)


def elder_lv2_talk(self, warrior):
    def callback():
        items.SteelSword().used_by(warrior)
        items.game.map.array[2][10][7] = items.Floor()

    items.game.process_talk(items.game.info["creature_info"]["Elder"]["dialog"][0], callback)


def merchant_lv2_talk(self, warrior):
    def callback():
        items.SteelShield().used_by(warrior)
        items.game.map.array[2][10][9] = items.Floor()

    items.game.process_talk(items.game.info["creature_info"]["Merchant"]["dialog"][0], callback)


def shop_lv3_talk(self, warrior):
    items.game.process_shop("gold", 25, [800, 4, 4], True)


def thief_lv4_talk(self, warrior):
    if items.game.info["indicator"]["thief_lv4_talk"] == 0:
        thief_lv4_talk1(self, warrior)
        items.game.info["indicator"]["thief_lv4_talk"] = 1
    elif items.game.info["indicator"]["thief_lv4_talk"] == 1:
        thief_lv4_talk2(self, warrior)
        items.game.info["indicator"]["thief_lv4_talk"] = 2


def thief_lv4_talk1(self, warrior):
    def callback():
        items.game.map.array[2][6][1] = items.Floor()

    items.game.process_talk(items.game.info["creature_info"]["Thief"]["dialog"][0], callback)


def thief_lv4_talk2(self, warrior):
    def callback():
        items.game.map.array[18][8][5] = items.Floor()
        items.game.map.array[18][9][5] = items.Floor()
        items.game.map.array[4][0][5] = items.Floor()

    if items.game.info["indicator"]["warrior_get_hoe"]:
        items.game.process_talk(items.game.info["creature_info"]["Thief"]["dialog"][1], callback)


def elder_lv5_talk(self, warrior):
    items.game.process_shop("exp", [100, 30, 30], [1, 5, 5])


def merchant_lv5_talk(self, warrior):
    items.game.process_shop("key", [10, 50, 100], [1, 1, 1])


def shop_lv11_talk(self, warrior):
    items.game.process_shop("gold", 100, [4000, 20, 20])


def merchant_lv12_talk(self, warrior):
    items.game.process_shop("key_sell", [7, 35, 70], [1, 1, 1])


def elder_lv13_talk(self, warrior):
    items.game.process_shop("exp", [270, 95, 95], [3, 17, 17])


def elder_lv15_talk(self, warrior):
    def callback1():
        items.game.warrior.exp -= 500
        items.SacredSword().used_by(items.game.warrior)
        items.game.map.array[15][3][4] = items.Floor()

    def callback():
        if items.game.warrior.exp >= 500:
            items.game.process_talk(items.game.info["creature_info"]["Elder"]["dialog"][2], callback1)
        else:
            items.game.process_talk(items.game.info["creature_info"]["Elder"]["dialog"][3])

    items.game.process_talk(items.game.info["creature_info"]["Elder"]["dialog"][1], callback)


def merchant_lv15_talk(self, warrior):
    def callback1():
        items.game.warrior.gold -= 500
        items.SacredShield().used_by(items.game.warrior)
        items.game.map.array[15][3][6] = items.Floor()

    def callback():
        if items.game.warrior.gold >= 500:
            items.game.process_talk(items.game.info["creature_info"]["Merchant"]["dialog"][2], callback1)
        else:
            items.game.process_talk(items.game.info["creature_info"]["Merchant"]["dialog"][3])

    items.game.process_talk(items.game.info["creature_info"]["Merchant"]["dialog"][1], callback)


def redboss_lv16_talk(self, warrior):
    items.game.process_talk(items.game.info["creature_info"]["RedBoss"]["dialog"][0])


def redboss_lv16_callback():
    adjust = ["SoulSolider", "DarkHeader", "SoulWizard", "RedBoss"]
    entries = ['hp', 'attack', 'defense', 'gold', 'exp']
    for obj in adjust:
        for entry in entries:
            items.game.info['creature_info'][obj][entry] = \
                math.floor(items.game.info['creature_info'][obj][entry] * 4 / 3)


def princess_lv18_talk(self, warrior):
    def callback():
        items.game.map.array[18][10][10] = items.UpStair()

    if items.game.info["indicator"]["princess_lv18_talk"] == 0:
        items.game.process_talk(items.game.info["creature_info"]["Princess"]["dialog"][0], callback)
        items.game.info["indicator"]["princess_lv18_talk"] = 1


def darkboss_lv19_talk(self, warrior):
    items.game.process_talk(items.game.info["creature_info"]["DarkBoss"]["dialog"][0])


def darkboss_lv19_callback():
    def callback():
        items.game.info['creature_info']['DarkBoss']['hp'] = 45000
        items.game.info['creature_info']['DarkBoss']['attack'] = 2550
        items.game.info['creature_info']['DarkBoss']['defense'] = 2250
        items.game.info['creature_info']['DarkBoss']['gold'] = 375
        items.game.info['creature_info']['DarkBoss']['exp'] = 330

    items.game.process_talk(items.game.info["creature_info"]["DarkBoss"]["dialog"][1], callback)


def darkboss_lv21_callback():
    def callback():
        items.game.status['win'] = True

    items.game.process_talk(items.game.info["creature_info"]["DarkBoss"]["dialog"][2], callback)


def add_dialog(npc, dialog):
    if issubclass(type(npc), items.Creature):
        npc.talk_to = dialog


def add_callback(npc, callback):
    if issubclass(type(npc), items.Creature):
        npc.callback = callback


def add_additional_attr(game):
    # add NPC dialogs
    add_dialog(game.map.array[0][8][5], test_talk)
    add_dialog(game.map.array[2][10][7], elder_lv2_talk)
    add_dialog(game.map.array[2][10][9], merchant_lv2_talk)
    add_dialog(game.map.array[3][0][5], shop_lv3_talk)
    add_dialog(game.map.array[4][0][5], thief_lv4_talk)
    add_dialog(game.map.array[5][7][1], elder_lv5_talk)
    add_dialog(game.map.array[5][3][10], merchant_lv5_talk)
    add_dialog(game.map.array[11][8][5], shop_lv11_talk)
    add_dialog(game.map.array[12][0][0], merchant_lv12_talk)
    add_dialog(game.map.array[13][6][4], elder_lv13_talk)
    add_dialog(game.map.array[15][3][4], elder_lv15_talk)
    add_dialog(game.map.array[15][3][6], merchant_lv15_talk)
    add_dialog(game.map.array[16][5][5], redboss_lv16_talk)
    add_callback(game.map.array[16][5][5], redboss_lv16_callback)
    add_dialog(game.map.array[18][4][5], princess_lv18_talk)
    add_dialog(game.map.array[19][6][5], darkboss_lv19_talk)
    add_callback(game.map.array[19][6][5], darkboss_lv19_callback)
    add_callback(game.map.array[21][1][5], darkboss_lv21_callback)

    # adjust access of IronFence
    game.map.array[2][7][7].can_open = True
    game.map.array[2][7][9].can_open = True
    game.map.array[4][2][5].can_open = True
    game.map.array[7][4][4].can_open = True
    game.map.array[10][6][3].can_open = True
    game.map.array[13][6][3].can_open = True
    game.map.array[14][4][5].can_open = True
    game.map.array[18][5][5].can_open = True
    game.map.array[19][6][2].can_open = True
    game.map.array[19][6][8].can_open = True


