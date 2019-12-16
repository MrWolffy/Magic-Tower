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
    draw.speak(warrior, u'    ……', warrior.game)
    draw.speak(self, u'    你醒了！', warrior.game)
    draw.speak(warrior, u'    ……\n    你是谁？我在哪里？', warrior.game)
    draw.speak(self, u'    我是这里的仙子，刚才\n你被这里的小怪打昏了', warrior.game)
    draw.speak(warrior, u'    ……\n    剑，剑，我的剑呢？', warrior.game)
    draw.speak(self, u'    你的剑被他们抢走了，我\n只来得及将你救出来', warrior.game)
    draw.speak(warrior, u'    那，公主呢？我是来救\n公主的。', warrior.game)
    draw.speak(self, u'    公主还在里面，你这样进\n去是打不过里面的小怪的', warrior.game)
    draw.speak(warrior, u'    那我怎么办，我答应了\n国王一定要把公主救出来', warrior.game)
    draw.speak(warrior, u'的，那我现在应该怎么办\n呢？', warrior.game)
    draw.speak(self, u'    放心吧，我把我的力量借\n给你，你就可以打赢那些小', warrior.game)
    draw.speak(self, u'怪了。不过，你得先帮我去\n找一样东西，找到了再来这', warrior.game)
    draw.speak(self, u'里找我。', warrior.game)
    draw.speak(warrior, u'    找东西？找什么东西？', warrior.game)
    draw.speak(self, u'    是一个十字架，中间有一\n颗红色的宝石。', warrior.game)
    draw.speak(warrior, u'    那个东西有什么用吗？', warrior.game)
    draw.speak(self, u'    我本是这座塔守护者，可\n不久前，从北方来了一批恶', warrior.game)
    draw.speak(self, u'魔，他们占领了这座塔，并\n将我的魔力封在了这个十字', warrior.game)
    draw.speak(self, u'架里面，如果你能将它带出\n塔来，那我的魔力便会慢慢', warrior.game)
    draw.speak(self, u'地恢复，到那时我便可以把\n力量借给你去救出公主了。', warrior.game)
    draw.speak(self, u'    要记住：只有用我的魔力\n才可以打开二十一层的门。', warrior.game)
    draw.speak(warrior, u'    ……\n    好吧，我试试看。', warrior.game)
    draw.speak(self, u'    刚才我去看过了，你的剑\n被放在三楼，你的盾在五楼', warrior.game)
    draw.speak(self, u'上，而那个十字架被放在七\n楼。要到七楼，你得先取回', warrior.game)
    draw.speak(self, u'你的剑和盾。\n    另外，在塔里的其他楼层', warrior.game)
    draw.speak(self, u'上，还有一些存放了好几百\n年的宝剑和宝物，如果得到', warrior.game)
    draw.speak(self, u'它们，对于你对付这里面的\n怪物将有很大的帮助。', warrior.game)
    draw.speak(warrior, u'    ……\n    可是，我怎么进去呢？', warrior.game)
    draw.speak(self, u'    我这里有三把钥匙，你先\n拿去，在塔里面还有很多这', warrior.game)
    draw.speak(self, u'样的钥匙，你一定要珍惜使\n用。', warrior.game)
    draw.speak(self, u'勇敢的去吧，勇士！', warrior.game)

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


def thief_talk1(thief, warrior):
    warrior.game.map.array[2][6][1] = items.Floor({}, [2, 6, 1])
    thief.talk_to = thief_talk2


def thief_talk2(thief, warrior):
    if warrior.game.indicator.get('warrior_get_hoe'):
        # warrior.game.map.array[20][7][5] = items.UpStair({})
        thief.talk_to = thief_talk3
        pass


def thief_talk3(thief, warrior):
    pass


def add_additional_function(game):
    # add NPC dialogs
    game.map.array[0][8][5].talk_to = test_talk
    game.map.array[2][10][7].talk_to = elder_lv2_talk
    game.map.array[2][10][9].talk_to = merchant_lv2_talk
    game.map.array[3][0][5].talk_to = shop_lv3_talk
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


