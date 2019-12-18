# -*- coding: utf-8 -*-
import Library.items as items
import Library.draw as draw


def test_talk(self, warrior):
    warrior.keys[0] += 1
    warrior.keys[1] += 1
    warrior.keys[2] += 1
    warrior.game.map.array[0][8][5] = items.Floor({}, self.position)
    warrior.game.map.array[0][8][4] = self
    self.position = [0, 8, 4]
    self.talk_to = fairy_lv0_talk2


def fairy_lv0_talk1(self, warrior):
    dialog = items.info["creature_info"]["Fairy"]["dialog"][0]
    for item in dialog:
        exec('draw.speak(' + item[0] + ', "' + item[1] + '", warrior.game)')

    warrior.keys[0] += 1
    warrior.keys[1] += 1
    warrior.keys[2] += 1
    warrior.game.map.array[0][8][5] = items.Floor({}, self.position)
    warrior.game.map.array[0][8][4] = self
    self.talk_to = fairy_lv0_talk2


def fairy_lv0_talk2(self, warrior):
    if warrior.game.indicator.get('warrior_get_cross'):
        warrior.game.map.array[20][7][5] = items.UpStair({}, [20, 7, 5])


def elder_lv2_talk(self, warrior):
    items.SteelSword({}, [0, 0, 0]).used_by(warrior)
    warrior.game.map.array[2][10][7] = items.Floor({}, [2, 10, 7])


def merchant_lv2_talk(self, warrior):
    items.SteelShield({}, [0, 0, 0]).used_by(warrior)
    warrior.game.map.array[2][10][9] = items.Floor({}, [2, 10, 9])


def shop_lv3_talk(self, warrior):
    if not warrior.game.indicator.get('first_use_shop'):
        draw.draw_shop_welcome(warrior)
    draw.draw_shop_interface(warrior, 25, [800, 4, 4])


def thief_talk1(self, warrior):
    dialog = items.info["creature_info"]["Thief"]["dialog"][0]
    for item in dialog:
        exec('draw.speak(' + item[0] + ', "' + item[1] + '", warrior.game)')

    warrior.game.map.array[2][6][1] = items.Floor({}, [2, 6, 1])
    self.talk_to = thief_talk2


def thief_talk2(self, warrior):
    if warrior.game.indicator.get('warrior_get_hoe'):
        # warrior.game.map.array[20][7][5] = items.UpStair({})
        self.__delattr__('talk_to')


def thief_talk3(self, warrior):
    pass


def elder_lv5_talk(self, warrior):
    draw.draw_expshop_interface(warrior, [100, 30, 30], [1, 5, 5])


def merchant_lv5_talk(self, warrior):
    draw.draw_keyshop_interface(warrior, [10, 50, 100], [1, 1, 1])


def shop_lv11_talk(self, warrior):
    draw.draw_shop_interface(warrior, 100, [4000, 20, 20])


def add_additional_function(game):
    # add NPC dialogs
    game.map.array[0][8][5].talk_to = test_talk
    game.map.array[2][10][7].talk_to = elder_lv2_talk
    game.map.array[2][10][9].talk_to = merchant_lv2_talk
    game.map.array[3][0][5].talk_to = shop_lv3_talk
    game.map.array[4][0][5].talk_to = thief_talk1
    game.map.array[5][7][1].talk_to = elder_lv5_talk
    game.map.array[5][3][10].talk_to = merchant_lv5_talk
    game.map.array[11][8][5].talk_to = shop_lv11_talk

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


