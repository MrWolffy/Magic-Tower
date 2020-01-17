# -*- coding: utf-8 -*-
import json
import pygame
import math
import time
from Library.others import *
import random

# structure of objects:
#
# Item
#   Floor
#   Barrier: Wall, Lava, Star
#   Door: YellowDoor, BlueDoor, RedDoor, SpecialDoor, IronFence
#   Prop
#       Bottle: RedBottle, BlueBottle
#       Key: YellowKey, BlueKey, RedKey, KeyKit
#       Gem: RedGem, BlueGem
#       Equipment
#           Sword: IronSword, SteelSword, QingFengSword, SacredSword
#           Shield: IronShield, SteelShield, GoldenShield, SacredShield
#       OtherProp: SmallWing, GoldCoin, BigWing, HolyWater
#       Special: Detector, Cross, Aircraft, Hoe
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


info = json.loads(''.join(open('Library/tower.json').readlines()))


class Item:
    def __init__(self):
        pass


class Floor(Item):
    def __init__(self):
        super().__init__()


class Barrier(Item):
    def __init__(self):
        super().__init__()


class Wall(Barrier):
    def __init__(self):
        super().__init__()


class Lava(Barrier):
    def __init__(self):
        super().__init__()


class Star(Barrier):
    def __init__(self):
        super().__init__()


class Door(Item):
    def __init__(self):
        super().__init__()


class YellowDoor(Door):
    def __init__(self):
        super().__init__()


class BlueDoor(Door):
    def __init__(self):
        super().__init__()


class RedDoor(Door):
    def __init__(self):
        super().__init__()


class SpecialDoor(Door):
    def __init__(self):
        super().__init__()


class IronFence(Door):
    def __init__(self):
        super().__init__()
        self.can_open = False


class Prop(Item):
    def __init__(self):
        super().__init__()


class Bottle(Prop):
    def __init__(self):
        super().__init__()


class RedBottle(Bottle):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.hp += 200


class BlueBottle(Bottle):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.hp += 500


class Key(Prop):
    def __init__(self):
        super().__init__()


class YellowKey(Key):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.keys[0] += 1


class BlueKey(Key):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.keys[1] += 1


class RedKey(Key):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.keys[2] += 1


class KeyKit(Key):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.keys[0] += 1
        warrior.keys[1] += 1
        warrior.keys[2] += 1


class Gem(Prop):
    def __init__(self):
        super().__init__()


class RedGem(Gem):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.attack += 3


class BlueGem(Gem):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.defense += 3


class Equipment(Prop):
    def __init__(self):
        super().__init__()


class Sword(Equipment):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.attack += game.info['prop_info'][type(self).__name__]['buff']


class Shield(Equipment):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.defense += game.info['prop_info'][type(self).__name__]['buff']


class IronSword(Sword):
    def __init__(self):
        super().__init__()


class SteelSword(Sword):
    def __init__(self):
        super().__init__()


class QingFengSword(Sword):
    def __init__(self):
        super().__init__()


class SacredSword(Sword):
    def __init__(self):
        super().__init__()


class IronShield(Shield):
    def __init__(self):
        super().__init__()


class SteelShield(Shield):
    def __init__(self):
        super().__init__()


class GoldenShield(Shield):
    def __init__(self):
        super().__init__()


class SacredShield(Shield):
    def __init__(self):
        super().__init__()


class OtherProp(Prop):
    def __init__(self):
        super().__init__()


class SmallWing(OtherProp):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.level += 1
        warrior.hp += 1000
        warrior.attack += 10
        warrior.defense += 10


class GoldCoin(OtherProp):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.gold += 300


class BigWing(OtherProp):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.level += 3
        warrior.hp += 3000
        warrior.attack += 30
        warrior.defense += 30


class HolyWater(OtherProp):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        warrior.hp *= 2


class Special(Prop):
    def __init__(self):
        super().__init__()


class Detector(Special):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        game.info['indicator']['warrior_get_detector'] = True
        instruction = game.info["prop_info"]["Detector"]
        game.process_instruction(instruction["chinese_name"], instruction["description"])


class Cross(Special):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        game.info['indicator']['warrior_get_cross'] = True
        instruction = game.info["prop_info"]["Cross"]
        game.process_instruction(instruction["chinese_name"], instruction["description"])


class Aircraft(Special):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        game.info['indicator']['warrior_get_aircraft'] = True
        instruction = game.info["prop_info"]["Aircraft"]
        game.process_instruction(instruction["chinese_name"], instruction["description"])


class Hoe(Special):
    def __init__(self):
        super().__init__()

    def used_by(self, warrior):
        game.info['indicator']['warrior_get_hoe'] = True
        instruction = game.info["prop_info"]["Hoe"]
        game.process_instruction(instruction["chinese_name"], instruction["description"])


class Stair(Item):
    def __init__(self):
        super().__init__()


class UpStair(Stair):
    def __init__(self):
        super().__init__()


class DownStair(Stair):
    def __init__(self):
        super().__init__()


class Creature(Item):
    def __init__(self):
        super().__init__()


class NPC(Creature):
    def __init__(self):
        super().__init__()


class Fairy(NPC):
    def __init__(self):
        super().__init__()


class Elder(NPC):
    def __init__(self):
        super().__init__()


class Merchant(NPC):
    def __init__(self):
        super().__init__()


class Shop(NPC):
    def __init__(self):
        super().__init__()


class ShopLeft(NPC):
    def __init__(self):
        super().__init__()


class ShopRight(NPC):
    def __init__(self):
        super().__init__()


class Thief(NPC):
    def __init__(self):
        super().__init__()


class Princess(NPC):
    def __init__(self):
        super().__init__()


class Monster(Creature):
    def __init__(self):
        super().__init__()
        self.hp = info["creature_info"][type(self).__name__]['hp']


class Slime(Monster):
    def __init__(self):
        super().__init__()


class RedSlime(Slime):
    def __init__(self):
        super().__init__()


class GreenSlime(Slime):
    def __init__(self):
        super().__init__()


class BlackSlime(Slime):
    def __init__(self):
        super().__init__()


class BigSlime(Slime):
    def __init__(self):
        super().__init__()


class _Skeleton(Monster):
    def __init__(self):
        super().__init__()


class Skeleton(_Skeleton):
    def __init__(self):
        super().__init__()


class SkeletonSolider(_Skeleton):
    def __init__(self):
        super().__init__()


class SkeletonHeader(_Skeleton):
    def __init__(self):
        super().__init__()


class Wizard(Monster):
    def __init__(self):
        super().__init__()


class PrimaryWizard(Wizard):
    def __init__(self):
        super().__init__()


class AdvancedWizard(Wizard):
    def __init__(self):
        super().__init__()


class HempWizard(Wizard):
    def __init__(self):
        super().__init__()


class RedWizard(Wizard):
    def __init__(self):
        super().__init__()


class SoulWizard(Wizard):
    def __init__(self):
        super().__init__()


class _Orc(Monster):
    def __init__(self):
        super().__init__()


class Orc(_Orc):
    def __init__(self):
        super().__init__()


class OrcSolider(_Orc):
    def __init__(self):
        super().__init__()


class Bat(Monster):
    def __init__(self):
        super().__init__()


class SmallBat(Bat):
    def __init__(self):
        super().__init__()


class BigBat(Bat):
    def __init__(self):
        super().__init__()


class RedBat(Bat):
    def __init__(self):
        super().__init__()


class Solider(Monster):
    def __init__(self):
        super().__init__()


class PrimarySolider(Solider):
    def __init__(self):
        super().__init__()


class IntermediateSolider(Solider):
    def __init__(self):
        super().__init__()


class AdvancedSolider(Solider):
    def __init__(self):
        super().__init__()


class StoneMan(Solider):
    def __init__(self):
        super().__init__()


class WhiteSolider(Solider):
    def __init__(self):
        super().__init__()


class GoldGuard(Solider):
    def __init__(self):
        super().__init__()


class GoldHeader(Solider):
    def __init__(self):
        super().__init__()


class DoubleSwordSolider(Solider):
    def __init__(self):
        super().__init__()


class DarkGuard(Solider):
    def __init__(self):
        super().__init__()


class DarkSolider(Solider):
    def __init__(self):
        super().__init__()


class DarkHeader(Solider):
    def __init__(self):
        super().__init__()


class SoulSolider(Solider):
    def __init__(self):
        super().__init__()


class ShadowSolider(Solider):
    def __init__(self):
        super().__init__()


class Boss(Monster):
    def __init__(self):
        super().__init__()


class RedBoss(Boss):
    def __init__(self):
        super().__init__()


class DarkBoss(Boss):
    def __init__(self):
        super().__init__()


class Warrior(Item):
    def __init__(self):
        super().__init__()
        warrior_info = info["creature_info"]['Warrior']
        self.position = warrior_info['position']
        self.level = warrior_info['level']
        self.attack = warrior_info['attack']
        self.defense = warrior_info['defense']
        self.hp = warrior_info['hp']
        self.exp = warrior_info['exp']
        self.gold = warrior_info['gold']
        self.keys = warrior_info['keys']

    def move(self, key, game):
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
            return
        elif issubclass(next_type, Prop):
            next_obj.used_by(self)
            game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor()
            return
        elif issubclass(next_type, Stair):
            if next_type.__name__ == 'UpStair':
                self.move_to_new_floor(self.position[0] + 1, 'up', game.map)
                game.info['indicator']['visited'][self.position[0]] = True
            elif next_type.__name__ == 'DownStair':
                self.move_to_new_floor(self.position[0] - 1, 'down', game.map)
            return
        elif issubclass(next_type, Monster):
            if hasattr(next_obj, 'talk_to'):
                next_obj.talk_to(next_obj, self)
                next_obj.__delattr__('talk_to')
                return
            flag, est_damage = self.can_beat(next_type.__name__)
            if flag:
                self.fight_with(next_obj)
                self.exp += game.info['creature_info'][next_type.__name__]['exp']
                self.gold += game.info['creature_info'][next_type.__name__]['gold']
                game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor()
                if hasattr(next_obj, 'callback'):
                    next_obj.callback(next_obj, self)
                    next_obj.__delattr__('callback')
            return
        elif issubclass(next_type, NPC):
            if hasattr(next_obj, 'talk_to'):
                next_obj.talk_to(next_obj, self)
            return
        game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = self
        game.map.array[self.position[0]][self.position[1]][self.position[2]] = Floor()
        self.position = next_pos

    def move_to_new_floor(self, level, mode, map):
        map.array[self.position[0]][self.position[1]][self.position[2]] = Floor()
        if mode == 'up':
            next_pos = [level, game.info['tower_structure']['up_position'][level][0],
                        game.info['tower_structure']['up_position'][level][1]]
        elif mode == 'down':
            next_pos = [level, game.info['tower_structure']['down_position'][level][0],
                        game.info['tower_structure']['down_position'][level][1]]
        self.position = next_pos.copy()
        map.array[self.position[0]][self.position[1]][self.position[2]] = self

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

    def fight_with(self, monster: Monster):
        monster_name = type(monster).__name__
        if monster_name == 'HempWizard':
            self.hp -= 100
        elif monster_name == 'RedWizard':
            self.hp -= 300
        elif monster_name == 'WhiteSolider':
            self.hp -= math.floor(self.hp / 4)
        elif monster_name == 'SoulWizard':
            self.hp -= math.floor(self.hp / 3)
        my_damage_per_round = self.attack - game.info['creature_info'][monster_name]['defense']
        monster_damage_per_round = max(game.info['creature_info'][monster_name]['attack'] - self.defense, 0)
        while monster.hp > 0:
            rand = random.random()
            if rand < self.level * 0.005:
                monster.hp = max(monster.hp - 2 * my_damage_per_round, 0)
            else:
                monster.hp = max(monster.hp - my_damage_per_round, 0)
            self.hp -= monster_damage_per_round


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
    def __init__(self, info):
        self.info = info
        tower_structure = info['tower_structure']
        creature_info = info['creature_info']
        level = tower_structure['total_level']
        height = tower_structure['height']
        width = tower_structure['width']
        map = Container(level, height, width)
        for i in range(level):
            for j in range(height):
                for k in range(width):
                    map.array[i][j][k] = eval(tower_structure['level_structure'][i][j][k] + '()')
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
            "win": False
        }
        add_additional_attr(self)

    def process_event(self, event):
        if self.status["instruction"]["display"]:
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
                    dialog["callback"].__call__()
                return
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
            if aircraft["welcome"]:
                if event.key == pygame.K_SPACE or event.key == pygame.K_5:
                    aircraft["welcome"] = False
            else:
                if event.key == pygame.K_SPACE or event.key == pygame.K_5:
                    # if self.info["indicator"]["visited"][aircraft["highlight"] + 1]:
                    #     self.warrior.move_to_new_floor(aircraft["highlight"] + 1, "up", self.map)
                    # else:
                    #     self.warrior.move_to_new_floor(self.warrior.position[0], "up", self.map)
                    self.warrior.move_to_new_floor(aircraft["highlight"] + 1, "up", self.map)
                    aircraft["display"] = False
                    aircraft["highlight"] = None
                elif event.key == pygame.K_2:
                    aircraft["highlight"] = (aircraft["highlight"] + 1) % 20
                elif event.key == pygame.K_8:
                    aircraft["highlight"] = (aircraft["highlight"] - 1) % 20
        else:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                game.warrior.move(event.key, game)
            elif event.key == pygame.K_a:
                pass
            elif event.key == pygame.K_s:
                pass
            elif event.key == pygame.K_r:
                pass
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


game = Game(info)
