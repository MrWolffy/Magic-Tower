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


t0 = time.process_time()
info = json.loads(''.join(open('Library/tower.json').readlines()))


class Item:
    def __init__(self, creature_info: dict, position):
        self.position = position


class Floor(Item):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Barrier(Item):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Wall(Barrier):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Lava(Barrier):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Star(Barrier):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Door(Item):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class YellowDoor(Door):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class BlueDoor(Door):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class RedDoor(Door):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SpecialDoor(Door):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class IronFence(Door):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)
        self.can_open = False


class Prop(Item):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Bottle(Prop):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class RedBottle(Bottle):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.hp += 200


class BlueBottle(Bottle):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.hp += 500


class Key(Prop):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class YellowKey(Key):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.keys[0] += 1


class BlueKey(Key):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.keys[1] += 1


class RedKey(Key):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.keys[2] += 1


class KeyKit(Key):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.keys[0] += 1
        warrior.keys[1] += 1
        warrior.keys[2] += 1


class Gem(Prop):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class RedGem(Gem):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.attack += 3


class BlueGem(Gem):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.defense += 3


class Equipment(Prop):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Sword(Equipment):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.attack += info['prop_info'][type(self).__name__]['buff']


class Shield(Equipment):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.defense += info['prop_info'][type(self).__name__]['buff']


class IronSword(Sword):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SteelSword(Sword):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class QingFengSword(Sword):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SacredSword(Sword):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class IronShield(Shield):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SteelShield(Shield):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class GoldenShield(Shield):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SacredShield(Shield):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class OtherProp(Prop):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SmallWing(OtherProp):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.level += 1
        warrior.hp += 1000
        warrior.attack += 10
        warrior.defense += 10


class GoldCoin(OtherProp):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.gold += 300


class BigWing(OtherProp):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.level += 3
        warrior.hp += 3000
        warrior.attack += 30
        warrior.defense += 30


class HolyWater(OtherProp):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        warrior.hp *= 2


class Special(Prop):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Detector(Special):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        info['indicator']['warrior_get_detector'] = True


class Cross(Special):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        info['indicator']['warrior_get_cross'] = True


class Aircraft(Special):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        info['indicator']['warrior_get_aircraft'] = True


class Hoe(Special):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)

    def used_by(self, warrior):
        info['indicator']['warrior_get_hoe'] = True


class Stair(Item):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class UpStair(Stair):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class DownStair(Stair):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Creature(Item):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class NPC(Creature):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Fairy(NPC):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Elder(NPC):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Merchant(NPC):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Shop(NPC):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class ShopLeft(NPC):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class ShopRight(NPC):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Thief(NPC):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Princess(NPC):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Monster(Creature):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)
        self.hp = creature_info[type(self).__name__]['hp']


class Slime(Monster):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class RedSlime(Slime):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class GreenSlime(Slime):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class BlackSlime(Slime):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class BigSlime(Slime):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class _Skeleton(Monster):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Skeleton(_Skeleton):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SkeletonSolider(_Skeleton):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SkeletonHeader(_Skeleton):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Wizard(Monster):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class PrimaryWizard(Wizard):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class AdvancedWizard(Wizard):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class HempWizard(Wizard):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class RedWizard(Wizard):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SoulWizard(Wizard):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class _Orc(Monster):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Orc(_Orc):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class OrcSolider(_Orc):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Bat(Monster):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SmallBat(Bat):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class BigBat(Bat):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class RedBat(Bat):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Solider(Monster):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class PrimarySolider(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class IntermediateSolider(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class AdvancedSolider(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class StoneMan(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class WhiteSolider(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class GoldGuard(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class GoldHeader(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class DoubleSwordSolider(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class DarkGuard(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class DarkSolider(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class DarkHeader(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class SoulSolider(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class ShadowSolider(Solider):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Boss(Monster):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class RedBoss(Boss):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class DarkBoss(Boss):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)


class Warrior(Item):
    def __init__(self, creature_info: dict, position):
        super().__init__(creature_info, position)
        info = creature_info['Warrior']
        self.position = info['position']
        self.level = info['level']
        self.attack = info['attack']
        self.defense = info['defense']
        self.hp = info['hp']
        self.exp = info['exp']
        self.gold = info['gold']
        self.keys = info['keys']

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
                    game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = \
                        Floor({}, next_pos)
                return
            if self.keys[idx] != 0:
                self.keys[idx] -= 1
                game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({}, next_pos)
            return
        elif issubclass(next_type, Prop):
            next_obj.used_by(self)
            game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({}, next_pos)
            return
        elif issubclass(next_type, Stair):
            if next_type.__name__ == 'UpStair':
                self.move_to_new_floor(self.position[0] + 1, 'up', game.map)
                info['creature_info']['Warrior']['indicator']['visited'][self.position[0]] = True
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
                self.exp += info['creature_info'][next_type.__name__]['exp']
                self.gold += info['creature_info'][next_type.__name__]['gold']
                game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({}, next_pos)
                if hasattr(next_obj, 'callback'):
                    next_obj.callback(next_obj, self)
                    next_obj.__delattr__('callback')
            return
        elif issubclass(next_type, NPC):
            if hasattr(next_obj, 'talk_to'):
                next_obj.talk_to(next_obj, self)
            return
        game.map.array[next_pos[0]][next_pos[1]][next_pos[2]] = self
        game.map.array[self.position[0]][self.position[1]][self.position[2]] = Floor({}, self.position)
        self.position = next_pos

    def move_to_new_floor(self, level, mode, map):
        map.array[self.position[0]][self.position[1]][self.position[2]] = Floor({}, self.position)
        if mode == 'up':
            next_pos = [level, info['tower_structure']['up_position'][level][0],
                        info['tower_structure']['up_position'][level][1]]
        elif mode == 'down':
            next_pos = [level, info['tower_structure']['down_position'][level][0],
                        info['tower_structure']['down_position'][level][1]]
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
        if self.attack <= info['creature_info'][monster]['defense']:
            return False, "???"
        elif self.defense >= info['creature_info'][monster]['attack']:
            return True, monster_damage
        my_damage_per_round = self.attack - info['creature_info'][monster]['defense']
        monster_damage_per_round = info['creature_info'][monster]['attack'] - self.defense
        rounds_count = math.floor(info['creature_info'][monster]['hp'] / my_damage_per_round)
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
        my_damage_per_round = self.attack - info['creature_info'][monster_name]['defense']
        monster_damage_per_round = max(info['creature_info'][monster_name]['attack'] - self.defense, 0)
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
        global t0, info
        self.map = map
        self.warrior = warrior
        warrior.game = self
        t0 = time.process_time()
        self.indicator = {}
        self.info = info





