# -*- coding: utf-8 -*-
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
#       Equipment: IronSword, IronShield, SteelSword, SteelShield, QingFengSword
#                  GoldenShield, SacredSword, SacredShield
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


class Item:
    def __init__(self, item_info: dict):
        pass


class Floor(Item):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Barrier(Item):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Wall(Barrier):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Lava(Barrier):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Star(Barrier):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Door(Item):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class YellowDoor(Door):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class BlueDoor(Door):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class RedDoor(Door):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class SpecialDoor(Door):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class IronFence(Door):
    def __init__(self, item_info: dict):
        super().__init__(item_info)
        self.can_open = False


class Prop(Item):
    def __init__(self, item_info: dict):
        super().__init__(item_info)
        self.buff = ''


class Bottle(Prop):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class RedBottle(Bottle):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.hp += 200


class BlueBottle(Bottle):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.hp += 500


class Key(Prop):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class YellowKey(Key):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.keys[0] += 1


class BlueKey(Key):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.keys[1] += 1


class RedKey(Key):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.keys[2] += 1


class KeyKit(Key):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.keys[0] += 1
        warrior.keys[1] += 1
        warrior.keys[2] += 1


class Gem(Prop):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class RedGem(Gem):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.attack += 3


class BlueGem(Gem):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.defense += 3


class Equipment(Prop):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class IronSword(Equipment):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.attack += 10


class IronShield(Equipment):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.defense += 10


class SteelSword(Equipment):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.attack += 30


class SteelShield(Equipment):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.defense += 30


class QingFengSword(Equipment):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.attack += 70


class GoldenShield(Equipment):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.defense += 85


class SacredSword(Equipment):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.defense += 150


class SacredShield(Equipment):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.defense += 190


class OtherProp(Prop):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class SmallWing(OtherProp):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.level += 1
        warrior.hp += 1000
        warrior.attack += 10
        warrior.defense += 10


class GoldCoin(OtherProp):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.gold += 300


class BigWing(OtherProp):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.level += 3
        warrior.hp += 3000
        warrior.attack += 30
        warrior.defense += 30


class HolyWater(OtherProp):
    def __init__(self, item_info: dict):
        super().__init__(item_info)

    def used_by(self, warrior):
        warrior.hp *= 2


class Special(Prop):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Detector(Special):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Cross(Special):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Aircraft(Special):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Hoe(Special):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Stair(Item):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class UpStair(Stair):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class DownStair(Stair):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Creature(Item):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class NPC(Creature):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Fairy(NPC):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Elder(NPC):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Merchant(NPC):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Shop(NPC):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class ShopLeft(NPC):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class ShopRight(NPC):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Thief(NPC):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Princess(NPC):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Monster(Creature):
    def __init__(self, item_info: dict):
        super().__init__(item_info)
        info = item_info[type(self).__name__]
        self.attack = info['attack']
        self.defense = info['defense']
        self.hp = info['hp']
        self.exp = info['exp']
        self.gold = info['gold']


class Slime(Monster):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class RedSlime(Slime):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class GreenSlime(Slime):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class BlackSlime(Slime):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class BigSlime(Slime):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class _Skeleton(Monster):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Skeleton(_Skeleton):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class SkeletonSolider(_Skeleton):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class SkeletonHeader(_Skeleton):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Wizard(Monster):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class PrimaryWizard(Wizard):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class AdvancedWizard(Wizard):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class HempWizard(Wizard):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class RedWizard(Wizard):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class SoulWizard(Wizard):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class _Orc(Monster):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Orc(_Orc):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class OrcSolider(_Orc):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Bat(Monster):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class SmallBat(Bat):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class BigBat(Bat):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class RedBat(Bat):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Solider(Monster):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class PrimarySolider(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class IntermediateSolider(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class AdvancedSolider(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class StoneMan(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class WhiteSolider(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class GoldGuard(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class GoldHeader(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class DoubleSwordSolider(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class DarkGuard(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class DarkSolider(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class DarkHeader(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class SoulSolider(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class ShadowSolider(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Boss(Monster):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class RedBoss(Boss):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class DarkBoss(Boss):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Warrior(Item):
    def __init__(self, item_info: dict):
        super().__init__(item_info)
        info = item_info['Warrior']
        self.position = info['position']
        self.level = info['level']
        self.attack = info['attack']
        self.defense = info['defense']
        self.hp = info['hp']
        self.exp = info['exp']
        self.gold = info['gold']
        self.keys = info['keys']

    def move(self, key, map):
        next_pos = {pygame.K_LEFT: [0, 0, -1],
                    pygame.K_RIGHT: [0, 0, 1],
                    pygame.K_UP: [0, -1, 0],
                    pygame.K_DOWN: [0, 1, 0]}[key]
        next_pos = [next_pos[i] + self.position[i] for i in range(3)]
        if next_pos[1] < 0 or next_pos[2] < 0 or next_pos[1] >= map.height or next_pos[2] >= map.width:
            return
        next_obj = map.array[next_pos[0]][next_pos[1]][next_pos[2]]
        next_type = type(next_obj)
        if issubclass(next_type, Barrier):
            return
        elif issubclass(next_type, Door):
            idx = {'YellowDoor': 0, 'BlueDoor': 1, 'RedDoor': 2}.get(next_type.__name__)
            if idx is None:
                if next_type.__name__ == 'IronFence' and next_obj.can_open:
                    map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({})
                return
            if self.keys[idx] != 0:
                self.keys[idx] -= 1
                map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({})
            return
        elif issubclass(next_type, Prop):
            if not issubclass(next_type, Special):
                next_obj.used_by(self)
            else:
                pass
            map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({})
            return
        elif issubclass(next_type, Stair):
            if next_type.__name__ == 'UpStair':
                self.move_to_new_floor(self.position[0] + 1, 'up', map)
            elif next_type.__name__ == 'DownStair':
                self.move_to_new_floor(self.position[0] - 1, 'down', map)
            return
        elif issubclass(next_type, Monster):
            flag, est_damage = self.can_beat(next_obj)
            if flag:
                self.fight_with(next_obj)
                self.exp += next_obj.exp
                self.gold += next_obj.gold
                map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({})
            return
        elif issubclass(next_type, NPC):
            next_obj.talk_to(next_obj, self, map)
            return
        map.array[next_pos[0]][next_pos[1]][next_pos[2]] = self
        map.array[self.position[0]][self.position[1]][self.position[2]] = Floor({})
        self.position = next_pos

    def move_to_new_floor(self, level, mode, map):
        map.array[self.position[0]][self.position[1]][self.position[2]] = Floor({})
        next_pos = [level, None, None]
        for j in range(len(map.array[level])):
            for k in range(len(map.array[level][j])):
                type_name = type(map.array[level][j][k]).__name__
                if (type_name == 'UpStair' and mode == 'down') or \
                        (type_name == 'DownStair' and mode == 'up'):
                    next_pos = [level, j, k]
                    break
        self.position = next_pos.copy()
        if next_pos[1] > 0 and issubclass(type(map.array[next_pos[0]][next_pos[1]-1][next_pos[2]]), Floor):
            self.position[1] -= 1   # up
        elif next_pos[2] < map.height - 1 and issubclass(type(map.array[next_pos[0]][next_pos[1]][next_pos[2]+1]), Floor):
            self.position[2] += 1   # right
        elif next_pos[2] > 0 and issubclass(type(map.array[next_pos[0]][next_pos[1]][next_pos[2]-1]), Floor):
            self.position[2] -= 1   # left
        elif next_pos[1] < map.height - 1 and issubclass(type(map.array[next_pos[0]][next_pos[1]+1][next_pos[2]]), Floor):
            self.position[1] += 1   # down
        map.array[self.position[0]][self.position[1]][self.position[2]] = self

    def can_beat(self, monster: Monster):
        monster_damage = 0
        monster_name = type(monster).__name__
        if monster_name == 'HempWizard':
            monster_damage += 100
        elif monster_name == 'RedWizard':
            monster_damage += 300
        elif monster_name == 'WhiteSolider':
            monster_damage += math.floor(self.hp / 4)
        elif monster_name == 'SoulWizard':
            monster_damage += math.floor(self.hp / 3)
        if self.attack <= monster.defense:
            return False, "???"
        elif self.defense >= monster.attack:
            return True, monster_damage
        my_damage_per_round = self.attack - monster.defense
        monster_damage_per_round = monster.attack - self.defense
        rounds_count = math.floor(monster.hp / my_damage_per_round)
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
        my_damage_per_round = self.attack - monster.defense
        monster_damage_per_round = max(monster.attack - self.defense, 0)
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
    def __init__(self, map: Container, warrior: Warrior):
        global ts
        self.map = map
        self.warrior = warrior
        ts = time.process_time()


ts = 0

