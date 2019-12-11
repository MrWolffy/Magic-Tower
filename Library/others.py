# -*- coding: utf-8 -*-
import Library.items as items


def fairy_talk1(fairy, warrior, map):
    warrior.keys[0] += 1
    warrior.keys[1] += 1
    warrior.keys[2] += 1
    map.array[0][8][5] = items.Floor({})
    map.array[0][8][4] = fairy
    fairy.talk_to = fairy_talk2


def fairy_talk2(self, warrior, map):
    pass


def elder_talk_lv2(self, warrior, map):
    items.SteelSword({}).used_by(warrior)
    map.array[2][10][7] = items.Floor({})


def merchant_talk_lv2(self, warrior, map):
    items.SteelShield({}).used_by(warrior)
    map.array[2][10][9] = items.Floor({})


def thief_talk1(thief, warrior, map):
    map.array[2][6][1] = items.Floor({})
    thief.talk_to = thief_talk2


def thief_talk2(thief, warrior, map):
    pass


def add_additional_function(game):
    # add NPC dialogs
    game.map.array[0][8][5].talk_to = fairy_talk1
    game.map.array[2][10][7].talk_to = elder_talk_lv2
    game.map.array[2][10][9].talk_to = merchant_talk_lv2
    game.map.array[4][0][5].talk_to = thief_talk1

    # adjust access of IronFence
    game.map.array[2][7][7].can_open = True
    game.map.array[2][7][9].can_open = True
    game.map.array[4][2][5].can_open = True
    game.map.array[10][6][3].can_open = True


