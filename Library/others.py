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


def fairy_lv0_talk1(self, warrior):
    def callback():
        warrior.keys[0] += 1
        warrior.keys[1] += 1
        warrior.keys[2] += 1
        items.game.map.array[0][8][5] = items.Floor()
        items.game.map.array[0][8][4] = self
        self.position = [0, 8, 4]
        self.talk_to = fairy_lv0_talk2

    items.game.process_talk(items.game.info["creature_info"]["Fairy"]["dialog"][0], callback)


def fairy_lv0_talk2(self, warrior):
    def callback():
        items.game.map.array[20][7][5] = items.UpStair()
        warrior.hp = math.floor(warrior.hp * 4 / 3)
        warrior.attack = math.floor(warrior.attack * 4 / 3)
        warrior.defense = math.floor(warrior.defense * 4 / 3)

    if items.game.info['indicator']['warrior_get_cross']:
        items.game.process_talk(items.game.info["creature_info"]["Fairy"]["dialog"][0], callback)


def elder_lv2_talk(self, warrior):
    def callback():
        items.SteelSword().used_by(warrior)
        warrior.game.map.array[2][10][7] = items.Floor()

    items.game.process_talk(items.game.info["creature_info"]["Elder"]["dialog"][0], callback)


def merchant_lv2_talk(self, warrior):
    def callback():
        items.SteelShield().used_by(warrior)
        warrior.game.map.array[2][10][9] = items.Floor()

    items.game.process_talk(items.game.info["creature_info"]["Merchant"]["dialog"][0], callback)


def shop_lv3_talk(self, warrior):
    items.game.process_shop("gold", 25, [800, 4, 4], True)


def thief_lv4_talk1(self, warrior):
    def callback():
        warrior.game.map.array[2][6][1] = items.Floor()
        self.talk_to = thief_lv4_talk2

    items.game.process_talk(items.game.info["creature_info"]["Thief"]["dialog"][0], callback)


def thief_lv4_talk2(self, warrior):
    def callback():
        warrior.game.map.array[18][8][5] = items.Floor()
        warrior.game.map.array[18][9][5] = items.Floor()
        warrior.game.map.array[4][0][5] = items.Floor()

    if warrior.game.indicator.get('warrior_get_hoe'):
        items.game.process_talk(items.game.info["creature_info"]["Thief"]["dialog"][1], callback)


def elder_lv5_talk(self, warrior):
    items.game.process_shop("exp", [100, 30, 30], [1, 5, 5])


def merchant_lv5_talk(self, warrior):
    items.game.process_shop("key", [100, 30, 30], [1, 5, 5])


def shop_lv11_talk(self, warrior):
    items.game.process_shop("gold", 100, [4000, 20, 20])


def merchant_lv12_talk(self, warrior):
    items.game.process_shop("key_sell", [7, 35, 70], [1, 1, 1])


def elder_lv13_talk(self, warrior):
    items.game.process_shop("exp", [270, 95, 95], [3, 17, 17])


def elder_lv15_talk(self, warrior):
    def callback():
        if warrior.exp >= 500:
            def callback1():
                warrior.exp -= 500
                items.SacredSword().used_by(warrior)
            items.game.process_talk(items.game.info["creature_info"]["Elder"]["dialog"][2], callback1)
        else:
            items.game.process_talk(items.game.info["creature_info"]["Elder"]["dialog"][2])

    items.game.process_talk(items.game.info["creature_info"]["Elder"]["dialog"][1], callback)


def merchant_lv15_talk(self, warrior):
    def callback():
        if warrior.gold >= 500:
            def callback1():
                warrior.gold -= 500
                items.SacredShield().used_by(warrior)
            items.game.process_talk(items.game.info["creature_info"]["Merchant"]["dialog"][2], callback1)
        else:
            items.game.process_talk(items.game.info["creature_info"]["Merchant"]["dialog"][3])

    items.game.process_talk(items.game.info["creature_info"]["Merchant"]["dialog"][1], callback)


def redboss_lv16_talk(self, warrior):
    items.game.process_talk(items.game.info["creature_info"]["RedBoss"]["dialog"][0])


def redboss_lv16_callback(self, warrior):
    adjust = ["SoulSoilder", "DarkHeader", "SoulWizard", "RedBoss"]
    entries = ['hp', 'attack', 'defense', 'gold', 'exp']
    for obj in adjust:
        for entry in entries:
            items.game.info['creature_info'][obj][entry] = \
                math.floor(items.game.info['creature_info'][obj][entry] * 4 / 3)


def princess_lv18_talk(self, warrior):
    def callback():
        warrior.game.map.array[18][10][10] = items.UpStair()
        self.__delattr__('talk_to')

    items.game.process_talk(items.game.info["creature_info"]["Princess"]["dialog"][0], callback)


def darkboss_lv19_talk(self, warrior):
    items.game.process_talk(items.game.info["creature_info"]["DarkBoss"]["dialog"][0])


def darkboss_lv19_callback(self, warrior):
    def callback():
        items.game.info['creature_info']['DarkBoss']['hp'] = 45000
        items.game.info['creature_info']['DarkBoss']['attack'] = 2550
        items.game.info['creature_info']['DarkBoss']['defense'] = 2250
        items.game.info['creature_info']['DarkBoss']['gold'] = 375
        items.game.info['creature_info']['DarkBoss']['exp'] = 330

    items.game.process_talk(items.game.info["creature_info"]["DarkBoss"]["dialog"][1], callback)


def darkboss_lv21_callback(self, warrior):
    def callback():
        items.game.status['win'] = True

    items.game.process_talk(items.game.info["creature_info"]["DarkBoss"]["dialog"][2], callback)


def add_additional_attr(game):
    # add NPC dialogs
    game.map.array[0][8][5].talk_to = test_talk
    game.map.array[2][10][7].talk_to = elder_lv2_talk
    game.map.array[2][10][9].talk_to = merchant_lv2_talk
    game.map.array[3][0][5].talk_to = shop_lv3_talk
    game.map.array[4][0][5].talk_to = thief_lv4_talk1
    game.map.array[5][7][1].talk_to = elder_lv5_talk
    game.map.array[5][3][10].talk_to = merchant_lv5_talk
    game.map.array[11][8][5].talk_to = shop_lv11_talk
    game.map.array[12][0][0].talk_to = merchant_lv12_talk
    game.map.array[13][6][4].talk_tp = elder_lv13_talk
    game.map.array[15][3][4].talk_to = elder_lv15_talk
    game.map.array[15][3][6].talk_to = merchant_lv15_talk
    game.map.array[16][5][5].talk_to = redboss_lv16_talk
    game.map.array[16][5][5].callback = redboss_lv16_callback
    game.map.array[19][7][5].talk_to = darkboss_lv19_talk
    game.map.array[19][7][5].callback = darkboss_lv19_callback
    game.map.array[21][1][5].callback = darkboss_lv21_callback

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


