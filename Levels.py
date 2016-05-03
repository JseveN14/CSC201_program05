#Jessica Neves
from Treasure_Class import *
from Character import *
import random #random generates positions

class Level(object):
    def __init__(self):
        self.level = []
        self.width = 40
        self.height = 25
        self.list_treasures = []
        self.treasure_locations = []
        self.stairs_up = []
        self.stairs_down = []
        self.foods = []
        self.weapons = []
        self.armors = []
        self.gold = []
        self.commands = {}
        self.player_x = []
        self.player_y = []

    #creates a level grid with nested lists
    def create_level(self):
        for rows in range(0, self.height):
            new_row = []
            for column in range(0, self.width):
                if (rows == 0) or (rows == self.height-1):
                    new_row.append('#')
                else:
                    if column == 0:
                        new_row.append('#')
                    elif column == self.width-1:
                        new_row.append('#')
                    else:
                        new_row.append('.')
            (self.level).append(new_row)

    #prints a neat grid without brackets or commas
    def display_level(self):
        for rows in self.level:
            print(' '.join(str(n) for n in rows))

    #makes a list of treasure items to be used in the level
    def level_treasures(self):
        (self.foods).append(Food("apple", 5, "a red, round fruit", 5))
        (self.foods).append(Food("bread", 10, "it's been baked, and has a hard "
                                 " outer crust", 10))
        (self.foods).append(Food("flask of water", 5, "it's a clean, drinkable "
                                 "liquid", 5))
        (self.foods).append(Food("ham", 10, "the cooked meat of a pig", 10))

        (self.weapons).append(Weapon("a knife", 5,
                                     "a small blade, sharp on one edge", 5))
        (self.weapons).append(Weapon("a sword", 15,
                                     "a long blade, sharp on both edges", 10))
        (self.weapons).append(Weapon("a club", 5,
                                     "a large, heavy piece of wood", 5))
        (self.weapons).append(Weapon("a dagger", 10,
                                     "a small blade, sharp on both edges", 5))

        (self.armors).append(Armor("padded leather", 15,
                                   "a jacket made from thick animal hide", 10))
        (self.armors).append(Armor("a chainmail shirt", 20,
                                   "small metal rings linked together to make "
                                   "a shirt",15))
        (self.armors).append(Armor("a small wooden shield", 15, "a circular "
                                   "piece of wood with a handle in the center "
                                   "of one side", 10))
        (self.armors).append(Armor("a helmet", 15, "a metal object for covering"
                                   " a fighter's head", 10))

        (self.gold).append(Gold("one gold coin", "a small shiny yellow coin",
                                1))
        (self.gold).append(Gold("five gold coins", "a pile of 5 small shiny "
                                "yellow coins", 5))
        (self.gold).append(Gold("ten gold coins", "a pile of 10 small shiny "
                                "yellow coins", 10))
        (self.gold).append(Gold("fifteen gold coins", "a pile of 15 small shiny"
                                "yellow coins", 15))
        (self.gold).append(Gold("twenty gold coins", "a pile of 20 small shiny "
                                "yellow coins", 20))
        (self.gold).append(Gold("fifty gold coins", "a pile of 50 small shiny "
                                "yellow coins", 50))
        (self.list_treasures).append(random.choice(self.foods))
        (self.list_treasures).append(random.choice(self.weapons))
        (self.list_treasures).append(random.choice(self.armors))
        (self.list_treasures).append(random.choice(self.gold))

    #gives the player an original starting point
    def place_player(self, player):
        self.player = player
        pos_x = random.randint(1, self.width - 2)#sets the border within walls
        pos_y = random.randint(1, self.height - 2)#sets the border within walls
        position = self.level[pos_y][pos_x]
        placed = False
        while placed == False:
            if (self.level[pos_y][pos_x] == "."):#player spawns on empty space
                position = self.level[pos_y][pos_x] = "P"#P shows players spot
                player.setPosition(pos_x, pos_y)
                placed = True
            else:
                pos_x = random.randint(1, self.width - 2)
                pos_y = random.randint(1, self.height - 2)
                position = self.level[pos_y][pos_x]

    #updates P to a new location on the map
    def move_player(self, player):
        self.player = player
        pos_x = player.pos_x
        pos_y = player.pos_y
        position = self.level[pos_y][pos_x] = "P"
        (self.player_x).append(pos_x)
        (self.player_y).append(pos_y)

    #replaces P's previous location accordingly
    def replace_player(self):
        pos_x = self.player_x[0]
        pos_y = self.player_y[0]
        (self.player_x).remove(pos_x)
        (self.player_y).remove(pos_y)
        position = self.level[pos_y][pos_x]
        if position in self.treasure_locations:
            position = self.level[pos_y][pos_x] = "*"
        elif position in self.stairs_up:
            position = self.level[pos_y][pos_x] = "u"
        elif position in self.stairs_down:
            position = self.level[pos_y][pos_x] = "d"
        else:
            position = self.level[pos_y][pos_x] = "."
        
    #places randomly chosen treasure items around the map    
    def place_treasure(self):
        for treasure in self.list_treasures:
            pos_x = random.randint(1, self.width - 2)
            pos_y = random.randint(1, self.height - 2)
            position = self.level[pos_y][pos_x]
            placed = False
            while placed == False:
                if (self.level[pos_y][pos_x] == "."
                    and position not in self.treasure_locations):
                    position = self.level[pos_y][pos_x] = "*"
                    treasure.setPosition(pos_x, pos_y)
                    (self.treasure_locations).append(treasure.getPosition())
                    placed = True
                else:
                    pos_x = random.randint(1, self.width - 2)
                    pos_y = random.randint(1, self.height - 2)
                    position = self.level[pos_y][pos_x]

    #places the stairs to next level
    def stair_up(self):
        pos_x = random.randint(1, self.width - 2)
        pos_y = random.randint(1, self.height - 2)
        position = self.level[pos_y][pos_x]
        placed = False
        while placed == False:
            if (position == "."):
                position = self.level[pos_y][pos_x]
                self.level[pos_y][pos_x] = "u"
                (self.stairs_up).append((pos_x, pos_y))
                placed = True
            else:
                pos_x = random.randint(1, self.width - 2)
                pos_y = random.randint(1, self.height - 2)
                position = self.level[pos_y][pos_x]

    #places the stairs to previous level
    def stair_down(self):
        pos_x = random.randint(1, self.width - 2)
        pos_y = random.randint(1, self.height - 2)
        position = self.level[pos_y][pos_x]
        placed = False
        while placed == False:
            if (position == "."):
                position = self.level[pos_y][pos_x]
                self.level[pos_y][pos_x] = "d"
                (self.stairs_down).append((pos_x, pos_y))
                placed = True
            else:
                pos_x = random.randint(1, self.width - 2)
                pos_y = random.randint(1, self.height - 2)
                position = self.level[pos_y][pos_x]
            
        
