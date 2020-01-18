# -*- coding: utf-8 -*-
import json
import pygame
import math
import time
from Library.others import add_additional_attr
import random
import os


# structure of objects:
#
# Item
#   Floor
#   Barrier: Wall, Lava, Star
#   Door: YellowDoor, BlueDoor, RedDoor, SpecialDoor, IronFence
#   Prop
#       Bottle: RedBottle, BlueBottle
#       Key: YellowKey, BlueKey, RedKey
#       Gem: RedGem, BlueGem
#       Equipment
#           Sword: IronSword, SteelSword, QingFengSword, SacredSword
#           Shield: IronShield, SteelShield, GoldenShield, SacredShield
#       OtherProp: KeyKit, SmallWing, GoldCoin, BigWing
#       Special: Detector, Cross, Aircraft, Hoe, HolyWater
#   Stair: UpStair, DownStair
#   Creature
#       Monster
#           Slime: RedSlime, GreenSlime, BlackSlime, BigSlime
#           _Skeleton: Skeleton, SkeletonSolider, SkeletonHeader
#           Wizard: PrimaryWizard, AdvancedWizard, HempWizard, RedWizard, SoulWizard
#           _Orc: Orc, OrcSolider
#           Bat: SmallBat, BigBat, RedBat
#           Solider: PrimarySolider, AdvancedSolider, StoneMan, WhiteSolider,
#                    GoldGuard, GoldHeader, DoubleSwordSolider, DarkGuard, DarkSolider,
#                    DarkHeader, SoulSolider, ShadowSolider
#           Boss: RedBoss, DarkBoss
#       NPC: Fairy, Elder, Merchant, Shop, ShopLeft, ShopRight, Thief, Princess
#   Warrior


class Item:
    def __init__(self, info=None):
        pass


class Floor(Item):
    def __init__(self, info=None):
        super().__init__(info)


class Barrier(Item):
    def __init__(self, info=None):
        super().__init__(info)


class Wall(Barrier):
    def __init__(self, info=None):
        super().__init__(info)


class Lava(Barrier):
    def __init__(self, info=None):
        super().__init__(info)


class Star(Barrier):
    def __init__(self, info=None):
        super().__init__(info)


class Door(Item):
    def __init__(self, info=None):
        super().__init__(info)


class YellowDoor(Door):
    def __init__(self, info=None):
        super().__init__(info)


class BlueDoor(Door):
    def __init__(self, info=None):
        super().__init__(info)


class RedDoor(Door):
    def __init__(self, info=None):
        super().__init__(info)


class SpecialDoor(Door):
    def __init__(self, info=None):
        super().__init__(info)


class IronFence(Door):
    def __init__(self, info=None):
        super().__init__(info)
        self.can_open = False


class Prop(Item):
    def __init__(self, info=None):
        super().__init__(info)

    @staticmethod
    def generate_alert_from_prop(prop):
        message = '得到'
        prop_info = game.info["prop_info"][prop.__name__]
        type_name = prop_info["chinese_name"]
        buff = str(prop_info.get("buff"))
        if issubclass(prop, Bottle):
            # 得到一个大血瓶 生命加 500 ！
            message = ' '.join([message + '一个' + type_name, '生命加', buff])
        elif issubclass(prop, Key):
            # 得到一把 黄钥匙！
            message = ' '.join([message + '一把', type_name])
        elif issubclass(prop, Gem):
            # 得到一个红宝石 攻击力加 3 ！
            message = message + '一个' + type_name
            if prop == BlueGem:
                message = ' '.join([message, '防御力加', buff])
            elif prop == RedGem:
                message = ' '.join([message, '攻击力加', buff])
        elif issubclass(prop, Sword):
            # 得到铁剑 攻击加 10 ！
            message = ' '.join([message + type_name, '攻击加', buff])
        elif issubclass(prop, Shield):
            # 得到铁盾 防御加 10 ！
            message = ' '.join([message + type_name, '防御加', buff])
        elif issubclass(prop, OtherProp):
            if prop == KeyKit:
                # 得到 钥匙盒 各种钥匙数加 1 ！
                message = ' '.join([message, type_name, '各种钥匙数加', buff])
            elif prop == SmallWing:
                # 得到 小飞羽 等级提升一级 ！
                message = ' '.join([message, type_name, '等级提升', buff, '级'])
            elif prop == GoldCoin:
                # 得到 金块 金币数加 300 ！
                message = ' '.join([message, type_name, '金币数加', buff])
            elif prop == BigWing:
                # 得到 大飞羽 等级提升三级 ！
                message = ' '.join([message, type_name, '等级提升', buff, '级'])
        return message + ' ！'


class Bottle(Prop):
    def __init__(self, info=None):
        super().__init__(info)


class RedBottle(Bottle):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.hp += game.info["prop_info"]["RedBottle"]["buff"]


class BlueBottle(Bottle):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.hp += game.info["prop_info"]["BlueBottle"]["buff"]


class Key(Prop):
    def __init__(self, info=None):
        super().__init__(info)


class YellowKey(Key):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.keys[0] += 1


class BlueKey(Key):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.keys[1] += 1


class RedKey(Key):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.keys[2] += 1


class Gem(Prop):
    def __init__(self, info=None):
        super().__init__(info)


class RedGem(Gem):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.attack += game.info["prop_info"]["RedGem"]["buff"]


class BlueGem(Gem):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.defense += game.info["prop_info"]["BlueGem"]["buff"]


class Equipment(Prop):
    def __init__(self, info=None):
        super().__init__(info)


class Sword(Equipment):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.attack += game.info['prop_info'][type(self).__name__]['buff']


class Shield(Equipment):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.defense += game.info['prop_info'][type(self).__name__]['buff']


class IronSword(Sword):
    def __init__(self, info=None):
        super().__init__(info)


class SteelSword(Sword):
    def __init__(self, info=None):
        super().__init__(info)


class QingFengSword(Sword):
    def __init__(self, info=None):
        super().__init__(info)


class SacredSword(Sword):
    def __init__(self, info=None):
        super().__init__(info)


class IronShield(Shield):
    def __init__(self, info=None):
        super().__init__(info)


class SteelShield(Shield):
    def __init__(self, info=None):
        super().__init__(info)


class GoldenShield(Shield):
    def __init__(self, info=None):
        super().__init__(info)


class SacredShield(Shield):
    def __init__(self, info=None):
        super().__init__(info)


class OtherProp(Prop):
    def __init__(self, info=None):
        super().__init__(info)


class KeyKit(OtherProp):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        buff = game.info["prop_info"]["KeyKit"]["buff"]
        warrior.keys[0] += buff
        warrior.keys[1] += buff
        warrior.keys[2] += buff


class SmallWing(OtherProp):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        level = game.info["prop_info"]["SmallWing"]["buff"]
        warrior.level += level
        warrior.hp += level * 1000
        warrior.attack += level * 10
        warrior.defense += level * 10


class GoldCoin(OtherProp):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.gold += game.info["prop_info"]["GoldCoin"]["buff"]


class BigWing(OtherProp):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        level = game.info["prop_info"]["BigWing"]["buff"]
        warrior.level += level
        warrior.hp += level * 1000
        warrior.attack += level * 10
        warrior.defense += level * 10


class Special(Prop):
    def __init__(self, info=None):
        super().__init__(info)


class Detector(Special):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        game.info['indicator']['warrior_get_detector'] = True


class Cross(Special):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        game.info['indicator']['warrior_get_cross'] = True


class Aircraft(Special):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        game.info['indicator']['warrior_get_aircraft'] = True


class Hoe(Special):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        game.info['indicator']['warrior_get_hoe'] = True


class HolyWater(Special):
    def __init__(self, info=None):
        super().__init__(info)

    def used_by(self, warrior):
        warrior.hp *= 2


class Stair(Item):
    def __init__(self, info=None):
        super().__init__(info)


class UpStair(Stair):
    def __init__(self, info=None):
        super().__init__(info)


class DownStair(Stair):
    def __init__(self, info=None):
        super().__init__(info)


class Creature(Item):
    def __init__(self, info=None):
        super().__init__(info)


class NPC(Creature):
    def __init__(self, info=None):
        super().__init__(info)


class Fairy(NPC):
    def __init__(self, info=None):
        super().__init__(info)


class Elder(NPC):
    def __init__(self, info=None):
        super().__init__(info)


class Merchant(NPC):
    def __init__(self, info=None):
        super().__init__(info)


class Shop(NPC):
    def __init__(self, info=None):
        super().__init__(info)


class ShopLeft(NPC):
    def __init__(self, info=None):
        super().__init__(info)


class ShopRight(NPC):
    def __init__(self, info=None):
        super().__init__(info)


class Thief(NPC):
    def __init__(self, info=None):
        super().__init__(info)


class Princess(NPC):
    def __init__(self, info=None):
        super().__init__(info)


class Monster(Creature):
    def __init__(self, info=None):
        super().__init__(info)


class Slime(Monster):
    def __init__(self, info=None):
        super().__init__(info)


class RedSlime(Slime):
    def __init__(self, info=None):
        super().__init__(info)


class GreenSlime(Slime):
    def __init__(self, info=None):
        super().__init__(info)


class BlackSlime(Slime):
    def __init__(self, info=None):
        super().__init__(info)


class BigSlime(Slime):
    def __init__(self, info=None):
        super().__init__(info)


class _Skeleton(Monster):
    def __init__(self, info=None):
        super().__init__(info)


class Skeleton(_Skeleton):
    def __init__(self, info=None):
        super().__init__(info)


class SkeletonSolider(_Skeleton):
    def __init__(self, info=None):
        super().__init__(info)


class SkeletonHeader(_Skeleton):
    def __init__(self, info=None):
        super().__init__(info)


class Wizard(Monster):
    def __init__(self, info=None):
        super().__init__(info)


class PrimaryWizard(Wizard):
    def __init__(self, info=None):
        super().__init__(info)


class AdvancedWizard(Wizard):
    def __init__(self, info=None):
        super().__init__(info)


class HempWizard(Wizard):
    def __init__(self, info=None):
        super().__init__(info)


class RedWizard(Wizard):
    def __init__(self, info=None):
        super().__init__(info)


class SoulWizard(Wizard):
    def __init__(self, info=None):
        super().__init__(info)


class _Orc(Monster):
    def __init__(self, info=None):
        super().__init__(info)


class Orc(_Orc):
    def __init__(self, info=None):
        super().__init__(info)


class OrcSolider(_Orc):
    def __init__(self, info=None):
        super().__init__(info)


class Bat(Monster):
    def __init__(self, info=None):
        super().__init__(info)


class SmallBat(Bat):
    def __init__(self, info=None):
        super().__init__(info)


class BigBat(Bat):
    def __init__(self, info=None):
        super().__init__(info)


class RedBat(Bat):
    def __init__(self, info=None):
        super().__init__(info)


class Solider(Monster):
    def __init__(self, info=None):
        super().__init__(info)


class PrimarySolider(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class IntermediateSolider(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class AdvancedSolider(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class StoneMan(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class WhiteSolider(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class GoldGuard(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class GoldHeader(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class DoubleSwordSolider(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class DarkGuard(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class DarkSolider(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class DarkHeader(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class SoulSolider(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class ShadowSolider(Solider):
    def __init__(self, info=None):
        super().__init__(info)


class Boss(Monster):
    def __init__(self, info=None):
        super().__init__(info)


class RedBoss(Boss):
    def __init__(self, info=None):
        super().__init__(info)


class DarkBoss(Boss):
    def __init__(self, info=None):
        super().__init__(info)


class Warrior(Item):
    def __init__(self, info=None):
        super().__init__(info)
        warrior_info = info["creature_info"]['Warrior']
        self.position = warrior_info['position']
        self.level = warrior_info['level']
        self.attack = warrior_info['attack']
        self.defense = warrior_info['defense']
        self.hp = warrior_info['hp']
        self.exp = warrior_info['exp']
        self.gold = warrior_info['gold']
        self.keys = warrior_info['keys']

    def move(self, key):
        next_pos = {pygame.K_LEFT: [0, 0, -1],
                    pygame.K_RIGHT: [0, 0, 1],
                    pygame.K_UP: [0, -1, 0],
                    pygame.K_DOWN: [0, 1, 0]}[key]
        next_pos = [next_pos[i] + self.position[i] for i in range(3)]
        if next_pos[1] < 0 or next_pos[2] < 0 or next_pos[1] >= game.map.height or next_pos[2] >= game.map.width:
            return
        next_obj = game.map.array[next_pos[0]][next_pos[1]][next_pos[2]]
        next_type = type(next_obj)
        if issubclass(next_type, Barrier):
            return
        elif issubclass(next_type, Door):
            idx = {'YellowDoor': 0, 'BlueDoor': 1, 'RedDoor': 2}.get(next_type.__name__)
            if idx is None:
                if next_type.__name__ == 'IronFence' and next_obj.can_open:
                    game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor()
                return
            if self.keys[idx] != 0:
                self.keys[idx] -= 1
                game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor()
        elif issubclass(next_type, Prop):
            next_obj.used_by(self)
            game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor()
            if not issubclass(next_type, Special):
                game.process_alert(next_type.generate_alert_from_prop(next_type))
            else:
                instruction = game.info["prop_info"][next_type.__name__]
                game.process_instruction(instruction["chinese_name"], instruction["description"])
        elif issubclass(next_type, Stair):
            if next_type.__name__ == 'UpStair':
                self.move_to_new_floor(self.position[0] + 1, 'up')
                game.info['indicator']['visited'][self.position[0]] = True
            elif next_type.__name__ == 'DownStair':
                self.move_to_new_floor(self.position[0] - 1, 'down')
        elif issubclass(next_type, Monster):
            if hasattr(next_obj, 'talk_to'):
                next_obj.talk_to(next_obj, self)
                next_obj.__delattr__('talk_to')
                return
            flag, est_damage = self.can_beat(next_type.__name__)
            if flag:
                game.process_fight(next_obj, next_pos)
        elif issubclass(next_type, NPC):
            if hasattr(next_obj, 'talk_to'):
                next_obj.talk_to(next_obj, self)
        else:
            game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = self
            game.map.array[self.position[0]][self.position[1]][self.position[2]] = Floor()
            self.position = next_pos

    def move_to_new_floor(self, level, mode):
        game.map.array[self.position[0]][self.position[1]][self.position[2]] = Floor()
        if mode == 'up':
            next_pos = [level, game.info['tower_structure']['up_position'][level][0],
                        game.info['tower_structure']['up_position'][level][1]]
        elif mode == 'down':
            next_pos = [level, game.info['tower_structure']['down_position'][level][0],
                        game.info['tower_structure']['down_position'][level][1]]
        self.position = next_pos.copy()
        game.map.array[self.position[0]][self.position[1]][self.position[2]] = self

    def can_beat(self, monster):
        monster_damage = 0
        if monster == 'HempWizard':
            monster_damage += 100
        elif monster == 'RedWizard':
            monster_damage += 300
        elif monster == 'WhiteSolider':
            monster_damage += math.floor(self.hp / 4)
        elif monster == 'SoulWizard':
            monster_damage += math.floor(self.hp / 3)
        if self.attack <= game.info['creature_info'][monster]['defense']:
            return False, "???"
        elif self.defense >= game.info['creature_info'][monster]['attack']:
            return True, monster_damage
        my_damage_per_round = self.attack - game.info['creature_info'][monster]['defense']
        monster_damage_per_round = game.info['creature_info'][monster]['attack'] - self.defense
        rounds_count = math.floor(game.info['creature_info'][monster]['hp'] / my_damage_per_round)
        monster_damage += rounds_count * monster_damage_per_round
        return monster_damage < self.hp, monster_damage

    def after_fight(self, next_pos):
        monster = game.map.array[next_pos[0]][next_pos[1]][next_pos[2]]
        monster_name = type(monster).__name__
        self.exp += game.info['creature_info'][monster_name]['exp']
        self.gold += game.info['creature_info'][monster_name]['gold']
        game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor()
        message = ' '.join(['得到金币数',
                            str(game.info['creature_info'][monster_name]['exp']),
                            '经验值',
                            str(game.info['creature_info'][monster_name]['gold']),
                            '！'])
        game.process_alert(message)
        if hasattr(monster, 'callback'):
            monster.callback()
            monster.__delattr__('callback')


class Container:
    def __init__(self, level, height, width):
        self.level = level
        self.height = height
        self.width = width
        self.array = [[[None for _ in range(width)] for _ in range(height)] for _ in range(level)]

    def debug(self, level):
        print("level: {:d}".format(level + 1))
        print("-" * (self.height * 7 + 1))
        for j in range(self.height):
            print("| ", end="")
            for k in range(self.width):
                print(type(self.array[level][j][k]).__name__[0:4], end=' | ')
            print("\n" + "-" * (self.height * 7 + 1))


class Game:
    def __init__(self, info=None):
        self.info = info
        tower_structure = self.info['tower_structure']
        creature_info = self.info['creature_info']
        level = tower_structure['total_level']
        height = tower_structure['height']
        width = tower_structure['width']
        map = Container(level, height, width)
        for i in range(level):
            for j in range(height):
                for k in range(width):
                    map.array[i][j][k] = eval(tower_structure['level_structure'][i][j][k] + '(info)')
        warrior_position = creature_info['Warrior']['position']
        warrior = map.array[warrior_position[0]][warrior_position[1]][warrior_position[2]]
        self.map = map
        self.warrior = warrior
        self.t0 = time.process_time()
        self.t1 = 0
        self.status = {
            "instruction": {
                "display": False,
                "name": None,
                "content": None
            },
            "dialog": {
                "display": False,
                "talking": None,
                "content": None,
                "content_left": None,
                "callback": None
            },
            "shop": {
                "display": False,
                "highlight": None,
                "type": None,
                "price": None,
                "buff": None,
                "first_use": False
            },
            "detector": {
                "display": False
            },
            "aircraft": {
                "display": False,
                "welcome": False,
                "highlight": None
            },
            "alert": {
                "display": False,
                "content": None,
                "frame": 0
            },
            "fight": {
                "display": False,
                "monster": None,
                "warrior": None,
                "frame": 0,
                "round": 0,
                "my_damage_per_round": 0,
                "monster_damage_per_round": 0
            },
            "win": False
        }
        add_additional_attr(self)
        if os.path.exists('Library/save.json'):
            os.remove('Library/save.json')

    def process_event(self, event):
        if self.status["alert"]["display"]:
            return
        elif self.status["fight"]["display"]:
            return
        elif self.status["instruction"]["display"]:
            instruction = self.status["instruction"]
            if event.key == pygame.K_SPACE:
                instruction["display"] = False
                instruction["name"] = None
                instruction["content"] = None
        elif self.status["dialog"]["display"]:
            dialog = self.status["dialog"]
            if event.key == pygame.K_SPACE:
                if dialog["content_left"]:
                    dialog["talking"] = dialog["content_left"][0][0]
                    dialog["content"] = dialog["content_left"][0][1]
                    dialog["content_left"] = dialog["content_left"][1:]
                else:
                    dialog["display"] = False
                    dialog["talking"] = None
                    dialog["content"] = None
                    dialog["content_left"] = None
                    if dialog["callback"] is not None:
                        tmp = dialog["callback"]
                        dialog["callback"] = None
                        tmp.__call__()
        elif self.status["shop"]["display"]:
            shop = self.status["shop"]
            if self.status["shop"]["first_use"]:
                if event.key == pygame.K_SPACE or event.key == pygame.K_5:
                    self.status["shop"]["first_use"] = False
                return
            if event.key == pygame.K_SPACE or event.key == pygame.K_5:
                if shop["highlight"] == 3:
                    self.status["shop"]["display"] = False
                    self.status["shop"]["highlight"] = None
                    self.status["shop"]["type"] = None
                    self.status["shop"]["price"] = None
                    self.status["shop"]["buff"] = None
                    return
                else:
                    if shop["type"] == "gold" and self.warrior.gold >= shop["price"]:
                        self.warrior.gold -= shop["price"]
                        if shop["highlight"] == 0:
                            self.warrior.hp += shop["buff"][0]
                        elif shop["highlight"] == 1:
                            self.warrior.attack += shop["buff"][1]
                        elif shop["highlight"] == 2:
                            self.warrior.defense += shop["buff"][2]
                    elif shop["type"] == 'exp' and self.warrior.exp >= shop["price"][shop["highlight"]]:
                        self.warrior.exp -= shop["price"][shop["highlight"]]
                        if shop["highlight"] == 0:
                            self.warrior.level += shop["buff"][0]
                            self.warrior.hp += shop["buff"][0] * 1000
                            self.warrior.attack += shop["buff"][0] * 10
                            self.warrior.defense += shop["buff"][0] * 10
                        elif shop["highlight"] == 1:
                            self.warrior.attack += shop["buff"][1]
                        elif shop["highlight"] == 2:
                            self.warrior.defense += shop["buff"][2]
                    elif shop["type"] == "key" and self.warrior.gold >= shop["price"][shop["highlight"]]:
                        self.warrior.gold -= shop["price"][shop["highlight"]]
                        self.warrior.keys[shop["highlight"]] += shop["buff"][shop["highlight"]]
                    elif shop["type"] == "key_sell" and \
                            self.warrior.keys[shop["highlight"]] >= shop["buff"][shop["highlight"]]:
                        self.warrior.keys[shop["highlight"]] -= shop["buff"][shop["highlight"]]
                        self.warrior.gold += shop["price"][shop["highlight"]]
            elif event.key == pygame.K_2:
                shop["highlight"] = min(3, shop["highlight"] + 1)
            elif event.key == pygame.K_8:
                shop["highlight"] = max(0, shop["highlight"] - 1)
        elif self.status["detector"]["display"]:
            if event.key == pygame.K_l:
                self.status["detector"]["display"] = False
        elif self.status["aircraft"]["display"]:
            aircraft = self.status["aircraft"]
            if event.key == pygame.K_j:
                aircraft["display"] = False
                aircraft["highlight"] = None
                return
            if aircraft["welcome"]:
                if event.key == pygame.K_SPACE or event.key == pygame.K_5:
                    aircraft["welcome"] = False
            else:
                if event.key == pygame.K_SPACE or event.key == pygame.K_5:
                    if self.info["indicator"]["visited"][aircraft["highlight"] + 1]:
                        self.warrior.move_to_new_floor(aircraft["highlight"] + 1, "up")
                    else:
                        self.warrior.move_to_new_floor(self.warrior.position[0], "up")
                    # self.warrior.move_to_new_floor(aircraft["highlight"] + 1, "up")
                    aircraft["display"] = False
                    aircraft["highlight"] = None
                elif event.key == pygame.K_2:
                    aircraft["highlight"] = (aircraft["highlight"] + 1) % 20
                elif event.key == pygame.K_8:
                    aircraft["highlight"] = (aircraft["highlight"] - 1) % 20
        else:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                game.warrior.move(event.key)
            elif event.key == pygame.K_a:
                if os.path.exists('Library/save.json'):
                    self.process_load('Library/save.json')
            elif event.key == pygame.K_s:
                self.process_save()
                self.process_alert('保存数据成功 ！')
            elif event.key == pygame.K_r:
                self.process_load('Library/tower.json')
            elif event.key == pygame.K_l:
                if game.info['indicator']['warrior_get_detector']:
                    self.status["detector"]["display"] = True
            elif event.key == pygame.K_j:
                if game.info['indicator']['warrior_get_aircraft']:
                    self.status["aircraft"]["display"] = True
                    self.status["aircraft"]["welcome"] = True
                    self.status["aircraft"]["highlight"] = 0

    def process_instruction(self, name, instruction):
        self.status["instruction"]["display"] = True
        self.status["instruction"]["name"] = name
        self.status["instruction"]["content"] = instruction

    def process_talk(self, dialog, callback=None):
        if not dialog:
            if callback is not None:
                callback.__call__()
            return
        self.status["dialog"]["display"] = True
        self.status["dialog"]["talking"] = dialog[0][0]
        self.status["dialog"]["content"] = dialog[0][1]
        self.status["dialog"]["content_left"] = dialog[1:]
        self.status["dialog"]["callback"] = callback

    def process_shop(self, type, price, buff, first_use=False):
        self.status["shop"]["display"] = True
        self.status["shop"]["first_use"] = first_use
        self.status["shop"]["type"] = type
        self.status["shop"]["price"] = price
        self.status["shop"]["buff"] = buff
        self.status["shop"]["highlight"] = 0

    def process_save(self):
        # 存图
        tower_structure = self.info['tower_structure']
        for i in range(tower_structure['total_level']):
            for j in range(tower_structure['height']):
                for k in range(tower_structure['width']):
                    self.info['tower_structure']["level_structure"][i][j][k] = type(self.map.array[i][j][k]).__name__

        # 存勇士
        self.info["creature_info"]["Warrior"]["position"] = self.warrior.position
        self.info["creature_info"]["Warrior"]['level'] = self.warrior.level
        self.info["creature_info"]["Warrior"]['attack'] = self.warrior.attack
        self.info["creature_info"]["Warrior"]['defense'] = self.warrior.defense
        self.info["creature_info"]["Warrior"]['hp'] = self.warrior.hp
        self.info["creature_info"]["Warrior"]['exp'] = self.warrior.exp
        self.info["creature_info"]["Warrior"]['gold'] = self.warrior.gold
        self.info["creature_info"]["Warrior"]['keys'] = self.warrior.keys

        # 保存至文件
        with open('Library/save.json', 'w', encoding='utf8') as f:
            f.write(json.dumps(self.info))

    def process_load(self, path):
        self.info = json.loads(''.join(open(path).readlines()))
        tower_structure = self.info['tower_structure']
        for i in range(tower_structure['total_level']):
            for j in range(tower_structure['height']):
                for k in range(tower_structure['width']):
                    if type(self.map.array[i][j][k]).__name__ != tower_structure['level_structure'][i][j][k]:
                        self.map.array[i][j][k] = eval(tower_structure['level_structure'][i][j][k] + '(self.info)')
        warrior_position = self.info['creature_info']['Warrior']['position']
        warrior = self.map.array[warrior_position[0]][warrior_position[1]][warrior_position[2]]
        self.warrior = warrior
        add_additional_attr(self)

    def process_alert(self, content):
        self.status["alert"]["display"] = True
        self.status["alert"]["content"] = content
        self.status["alert"]["frame"] = 0

    def process_fight(self, monster, position):
        fight = self.status["fight"]
        fight["display"] = True
        monster_info = self.info['creature_info'][type(monster).__name__]
        fight["monster"] = {"name": type(monster).__name__,
                            "hp": monster_info['hp'],
                            "attack": monster_info['attack'],
                            "defense": monster_info['defense'],
                            "position": position}
        fight['warrior'] = {"hp": game.warrior.hp}
        fight['frame'] = 0
        fight['round'] = 0
        fight['my_damage_per_round'] = game.warrior.attack - fight['monster']['defense']
        fight['monster_damage_per_round'] = max(fight['monster']['attack'] - game.warrior.defense, 0)
        # 处理特殊怪物
        monster_name = type(monster).__name__
        if monster_name == 'HempWizard':
            fight['warrior']['hp'] -= 100
        elif monster_name == 'RedWizard':
            fight['warrior']['hp'] -= 300
        elif monster_name == 'WhiteSolider':
            fight['warrior']['hp'] -= math.floor(fight['warrior']['hp'] / 4)
        elif monster_name == 'SoulWizard':
            fight['warrior']['hp'] -= math.floor(fight['warrior']['hp'] / 3)

    def process_next_frame(self):
        if self.status["alert"]["display"]:
            self.status["alert"]["frame"] += 1
            if self.status["alert"]["frame"] >= 12:
                self.status["alert"]["display"] = False
                self.status["alert"]["content"] = None
                self.status["alert"]["frame"] = 0
        elif self.status["fight"]["display"]:
            self.status["fight"]["frame"] += 1
            if self.status["fight"]["frame"] % 4 == 0:
                # 如果怪被打死了
                if self.status["fight"]['monster']['hp'] <= 0:
                    next_pos = self.status['fight']['monster']['position']
                    self.warrior.after_fight(next_pos)
                    self.status["fight"]['display'] = False
                    self.status["fight"]['monster'] = None
                    self.warrior.hp = self.status["fight"]['warrior']['hp']
                    self.status["fight"]['warrior'] = None
                    self.status["fight"]['frame'] = 0
                    self.status["fight"]['round'] = 0
                    self.status["fight"]['my_damage_per_round'] = 0
                    self.status["fight"]['monster_damage_per_round'] = 0
                    return
                # 如果还在战斗
                if self.status["fight"]['round'] % 2 == 0:
                    # 人的回合
                    rand = random.random()
                    if rand < self.warrior.level * 0.005:
                        # 暴击
                        self.status["fight"]['monster']['hp'] = \
                            max(self.status["fight"]['monster']['hp'] -
                                2 * self.status["fight"]['my_damage_per_round'], 0)
                    else:
                        self.status["fight"]['monster']['hp'] = \
                            max(self.status["fight"]['monster']['hp'] -
                                self.status["fight"]['my_damage_per_round'], 0)
                else:
                    # 怪的回合
                    self.status["fight"]['warrior']['hp'] -= self.status["fight"]['monster_damage_per_round']
                self.status["fight"]['round'] += 1


game = Game(json.loads(''.join(open('Library/tower.json').readlines())))
