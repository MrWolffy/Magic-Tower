import pygame


class Item:
    # subclass: Floor, Barrier, Door, Stair, NPC, Creature
    def __init__(self, item_info: dict):
        pass


class Floor(Item):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Barrier(Item):
    # subclass: Wall, Lava, Star, Door
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
    # subclass: YellowDoor
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class YellowDoor(Door):
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
    # subclass: Warrior, Monster, NPC
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class NPC(Creature):
    # subclass: Fairy
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Fairy(NPC):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Warrior(Creature):
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
        next_type = type(map.array[next_pos[0]][next_pos[1]][next_pos[2]])
        if issubclass(next_type, Barrier):
            return
        map.array[next_pos[0]][next_pos[1]][next_pos[2]] = self
        map.array[self.position[0]][self.position[1]][self.position[2]] = Floor({})
        self.position = next_pos


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


class RedSlime(Monster):
    def __init__(self, item_info: dict):
        super().__init__(item_info)


class Container:
    def __init__(self, level, height, width):
        self.level = level
        self.height = height
        self.width = width
        self.array = [[[None for i in range(width)] for j in range(height)] for k in range(level)]

    def debug(self):
        for i in range(self.level):
            print("level: {:d}".format(i + 1))
            print("-" * (self.height * 7 + 1))
            for j in range(self.height):
                print("| ", end="")
                for k in range(self.width):
                    print(type(self.array[i][j][k]).__name__[0:4], end=' | ')
                print("\n" + "-" * (self.height * 7 + 1))


class Game:
    def __init__(self, map, warrior):
        self.map = map
        self.warrior = warrior
