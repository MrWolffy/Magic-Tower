# -*- coding: utf-8 -*-
import Library.items as items
import Library.draw as draw
import random


def fairy_lv0_talk1(self, warrior, map):
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'    ……')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    你醒了！')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'    ……\n    你是谁？我在哪里？')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    我是这里的仙子，刚才\n你被这里的小怪打昏了')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'    ……\n    剑，剑，我的剑呢？')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    你的剑被他们抢走了，我\n只来得及将你救出来')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'    那，公主呢？我是来救\n公主的。')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    公主还在里面，你这样进\n去是打不过里面的小怪的')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'    那我怎么办，我答应了\n国王一定要把公主救出来')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'的，那我现在应该怎么办\n呢？')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    放心吧，我把我的力量借\n给你，你就可以打赢那些小')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'怪了。不过，你得先帮我去\n找一样东西，找到了再来这')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'里找我。')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'    找东西？找什么东西？')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    是一个十字架，中间有一\n颗红色的宝石。')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'    那个东西有什么用吗？')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    我本是这座塔守护着，可\n不久前，从北方来了一批恶')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'魔，他们占领了这座塔，并\n将我的魔力封在了这个十字')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'架里面，如果你能将它带出\n塔来，那我的魔力便会慢慢')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'地恢复，到那时我便可以把\n力量借给你去救出公主了。')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    要记住：只有用我的魔力\n才可以打开二十一层的门。')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'    ……\n好吧，我试试看。')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    刚才我去看过了，你的剑\n被放在三楼，你的盾在五楼')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'上，而那个十字架被放在七\n楼。要到七楼，你得先取回')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'你的剑和盾。\n    另外，在塔里的其他楼层')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'上，还有一些存放了好几百\n年的宝剑和宝物，如果得到')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'它们，对于你对付这里面的\n怪物将有很大的帮助。')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(warrior, (warrior.position[1], warrior.position[2]), u'    ……\n    可是，我怎么进去呢？')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'    我这里有三把钥匙，你先\n拿去，在塔里面还有很多这')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'样的钥匙，你一定要珍惜使\n用。')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))
    draw.speak(self, (8, 5), u'勇敢的去吧，勇士！')
    draw.draw_map(map.array[warrior.position[0]], random.randint(0, 3))

    warrior.keys[0] += 1
    warrior.keys[1] += 1
    warrior.keys[2] += 1
    map.array[0][8][5] = items.Floor({})
    map.array[0][8][4] = self
    self.talk_to = fairy_lv0_talk2


def fairy_lv0_talk2(self, warrior, map, screen):
    if items.indicator.get('warrior_get_cross'):
        map.array[20][7][5] = items.UpStair({})


def elder_lv2_talk(self, warrior, map, screen):
    items.SteelSword({}).used_by(warrior)
    map.array[2][10][7] = items.Floor({})


def merchant_lv2_talk(self, warrior, map, screen):
    items.SteelShield({}).used_by(warrior)
    map.array[2][10][9] = items.Floor({})


def thief_talk1(thief, warrior, map):
    map.array[2][6][1] = items.Floor({})
    thief.talk_to = thief_talk2


def thief_talk2(thief, warrior, map):
    if items.indicator.get('warrior_get_hoe'):
        # map.array[20][7][5] = items.UpStair({})
        pass


def add_additional_function(game):
    # add NPC dialogs
    game.map.array[0][8][5].talk_to = fairy_lv0_talk1
    game.map.array[2][10][7].talk_to = elder_lv2_talk
    game.map.array[2][10][9].talk_to = merchant_lv2_talk
    game.map.array[4][0][5].talk_to = thief_talk1

    # adjust access of IronFence
    game.map.array[2][7][7].can_open = True
    game.map.array[2][7][9].can_open = True
    game.map.array[4][2][5].can_open = True
    game.map.array[10][6][3].can_open = True
    game.map.array[13][6][3].can_open = True
    game.map.array[14][4][5].can_open = True
    game.map.array[18][5][5].can_open = True
    game.map.array[19][6][2].can_open = True
    game.map.array[19][6][8].can_open = True


