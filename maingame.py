#Jessica Neves
from Character import *
from Treasure_Class import *
from Levels import *
import random
import os,time

def main():#main game loop
    clear = lambda: os.system('cls')#clear command
    #command list
    Commands = {
        'h':Player.move_to,#listing function as Player.move_to() calls it
        'j':Player.move_to,
        'k':Player.move_to,
        'l':Player.move_to,
        '^':0,
        'v':0,
        'i':Player.inventory,
        'E':Player.equip,
        'a':Armor.wear,
        'A':Player.remove,
        'w':Weapon.wield,
        'W':Player.unwield,
        'e':Player.eat,
        'd':Player.drop,
        'p':Player.pickup,
        '?':print}
    myWorld = []#stores new levels
    name = input("Name your adventurer: ")
    player = Player(name)#makes player
    print("Welcome to the world, " + player.name + ".")
    myWorld.append(Level())#first level appended
    myWorld[0].create_level()
    myWorld[0].level_treasures()
    myWorld[0].place_treasure()
    myWorld[0].stair_up()
    myWorld[0].place_player(player)
    myWorld[0].display_level()
    
    run = "on"
    while run == "on":#while loop keeps game running
        player_action = input("> ")
        args = player_action.split()
        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]:
                    if c == 'h':#checks key to adjust arguments for methods
                        Commands[c](player, "West")
                        commandFound = True
                        clear()
                        myWorld[0].move_player(player)
                        myWorld[0].replace_player()
                        myWorld[0].display_level()
                        break
                    if c == 'j':
                        Commands[c](player, "South")
                        commandFound = True
                        clear()
                        myWorld[0].move_player(player)
                        myWorld[0].replace_player()
                        myWorld[0].display_level()
                        break
                    if c == 'k':
                        Commands[c](player, "North")
                        commandFound = True
                        clear()
                        myWorld[0].move_player(player)
                        myWorld[0].replace_player()
                        myWorld[0].display_level()
                        break
                    if c == 'l':
                        Commands[c](player, "East")
                        commandFound = True
                        clear()
                        myWorld[0].move_player(player)
                        myWorld[0].replace_player()
                        myWorld[0].display_level()
                        break
            if not commandFound:
                print("That is not a valid command.")
        
    

main()#calls main()
