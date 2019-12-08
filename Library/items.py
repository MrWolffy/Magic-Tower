# -*- coding: utf-8 -*-
import pygame
import math

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
#       Special: Detector
#   Stair: UpStair, DownStair
#   Creature
#       Monster
#           Slime: RedSlime, GreenSlime, BlackSlime
#           _Skeleton: Skeleton, SkeletonSolider
#           Wizard: PrimaryWizard
#           _Orc: Orc
#           Bat: SmallBat
#           Solider: GoldGuard, GoldHeader
#       NPC: Fairy, Elder, Merchant
#   Warrior


class Item:
    # subclass: Floor, Barrier, Door, Prop, Stair, Creature, Warrior
    def __init__(self, item_info: dict):
        pass


class Floor(Item):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Barrier(Item):
    # subclass: Wall, Lava, Star
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
    # subclass: YellowDoor, BlueDoor, RedDoor
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


class Prop(Item):
    # subclass: Bottle, Key, Gem, Equipment, Special
    def __init__(self, item_info: dict):
        super().__init__(item_info)
        self.buff = ''


class Bottle(Prop):
    # subclass: RedBottle, BlueBottle
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
    # subclass: YellowKey, BlueKey, RedKey
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


class Gem(Prop):
    # subclass: RedGem, BlueGem
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


class Special(Prop):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Detector(Special):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Stair(Item):
    # subclass: UpStair, DownStair
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class UpStair(Stair):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class DownStair(Stair):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Creature(Item):
    # subclass: Monster, NPC
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class NPC(Creature):
    # subclass: Fairy
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


class Monster(Creature):
    # subclass: RedSlime ...
    def __init__(self, item_info: dict):
        super().__init__(item_info)
        info = item_info[type(self).__name__]
        self.attack = info['attack']
        self.defense = info['defense']
        self.hp = info['hp']
        self.exp = info['exp']
        self.gold = info['gold']


class Slime(Monster):
    # subclass: RedSlime, GreenSlime, BlackSlime
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


class _Skeleton(Monster):
    # subclass: Skeleton, SkeletonSolider
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Skeleton(_Skeleton):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class SkeletonSolider(_Skeleton):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Wizard(Monster):
    # subclass: PrimaryWizard
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class PrimaryWizard(Wizard):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class _Orc(Monster):
    # subclass: Orc
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Orc(_Orc):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Bat(Monster):
    # subclass: SmallBat
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class SmallBat(Bat):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Solider(Monster):
    # subclass: GoldGuard, GoldHeader
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class GoldGuard(Solider):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class GoldHeader(Solider):
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
        next_pos = [0, 0, 0]
        if key == pygame.K_LEFT:
            next_pos = [0, 0, -1]
        elif key == pygame.K_RIGHT:
            next_pos = [0, 0, 1]
        elif key == pygame.K_UP:
            next_pos = [0, -1, 0]
        elif key == pygame.K_DOWN:
            next_pos = [0, 1, 0]
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
                return
            if self.keys[idx] == 0:
                return
            else:
                self.keys[idx] -= 1
                map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({})
                return
        elif issubclass(next_type, Prop):
            if not issubclass(next_type, Special):
                next_obj.used_by(self)
                map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({})
            else:
                pass
            map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({})
            return
        elif issubclass(next_type, Stair):
            if next_type.__name__ == 'UpStair':
                self.move_to_new_floor(self.position[0] + 1, 'up', map)
                return
            elif next_type.__name__ == 'DownStair':
                self.move_to_new_floor(self.position[0] - 1, 'down', map)
                return
        elif issubclass(next_type, Monster):
            flag, est_damage = self.can_beat(next_obj)
            if flag:
                self.hp -= est_damage
                self.exp += next_obj.exp
                self.gold += next_obj.gold
                map.array[next_pos[0]][next_pos[1]][next_pos[2]] = Floor({})
                return
            else:
                return
        elif issubclass(next_type, NPC):
            pass
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
            self.position[1] -= 1
        elif next_pos[2] > 0 and issubclass(type(map.array[next_pos[0]][next_pos[1]][next_pos[2]-1]), Floor):
            self.position[2] -= 1
        elif next_pos[1] < map.height - 1 and issubclass(type(map.array[next_pos[0]][next_pos[1]+1][next_pos[2]]), Floor):
            self.position[1] += 1
        elif next_pos[2] > map.height - 1 and issubclass(type(map.array[next_pos[0]][next_pos[1]][next_pos[2]+1]), Floor):
            self.position[2] += 1
        map.array[self.position[0]][self.position[1]][self.position[2]] = self

    def can_beat(self, monster: Monster):
        if self.attack <= monster.defense:
            return False, "???"
        elif self.defense >= monster.attack:
            return True, 0
        my_damage_per_round = self.attack - monster.defense
        monster_damage_per_round = monster.attack - self.defense
        rounds_count = math.ceil(monster.hp / my_damage_per_round)
        monster_damage = rounds_count * monster_damage_per_round
        return monster_damage < self.hp, monster_damage


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
    def __init__(self, map, warrior):
        self.map = map
        self.warrior = warrior
