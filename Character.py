#Jessica Neves
from Treasure_Class import *

#the Player class
class Player:
    def __init__(self, name):#takes a name
        self.name = name
        self.experience = 0
        self.health = 10
        self.max_health = 10
        self.pos_x = 0
        self.pos_y = 0
        self.position = (self.pos_x, self.pos_y)
        self.defense = 0
        self.attack = 0
        self.player_inventory = []
        self.equip_list = []
        location = self.position
        self.gold_amnt = 0

    def getDefense(self):
        return self.defense

    def setDefense(self):
        self.defense += Armor.getDefense

    def getPosition(self):
        return self.position

    def setDefense(self, defense):
        self.defense 

    def setAttack(self, damage):
        self.attack += damage

    def setPosition(self, pos_x, pos_y):
        self.position = (pos_x, pos_y)

    #returns a statement about the players health, weapon, and armor
    def look_at(self):
        equip_list_pos = 0
        hasArmor = False
        hasWeapon = False
        hasEquipment = False
        if self.health == self.max_health:
            healthy = "looks perfectly healthy"
        if self.max_health < self.health < (self.max_health/2):
            healthy = "looks pretty healthy"
        if (self.max_health/2) < self.health < 0:
            healthy = "does not look very healthy"
        if len(self.equip_list) > 0:
            hasEquipment = True
            if hasEquipment == True:
                for equipment in self.equip_list:
                    if ((self.equip_list[equip_list_pos]).
                        get_type_treasure() == "Armor"):
                        ArmorName = self.equip_list[equip_list_pos].getName()
                        hasArmor = True
                    elif ((self.equip_list[equip_list_pos]).
                          get_type_treasure() == "Weapon"):
                        WeaponName = (self.equip_list[equip_list_pos]).getName()
                        hasWeapon = True
                    equip_list_pos += 1
                if hasArmor == True:
                    armor = "is wearing " + ArmorName
                elif hasArmor == False:
                    armor = "is not wearing any armor"
                if hasWeapon == True:
                    weapon = "wielding " + WeaponName
                elif hasWeapon == False:
                    weapon = "is not wielding any weapon"
                return ("%s is an adventurer, who %s, %s, and %s."
                        % (self.name, healthy, armor, weapon))     
        else:
            return ("%s is an adventurer, who %s and is not wearing armor or "
                    "wielding a weapon."
                   % (self.name, healthy))                    
                        
    #moves the player around the map     
    def move_to(self, position):
        if position == "North":
            if self.pos_y == 1:
                print("You cannot move your character in that direction.")
            else:
                self.pos_x += 0
                self.pos_y += -1
                self.setPosition(self.pos_x, self.pos_y)

        elif position == "South":
            if self.pos_y == 23:
                print("You cannot move your character in that direction.")
            else:
                self.pos_x += 0
                self.pos_y += 1
                self.setPosition(self.pos_x, self.pos_y)

        elif position == "East":
            if self.pos_x == 38:
                print("You cannot move your character in that direction.")
            else:
                self.pos_x += 1
                self.pos_y += 0
                self.setPosition(self.pos_x, self.pos_y)

        elif position == "West":
            if self.pos_x == 1:
                print("You cannot move your character in that direction.")
            else:
                self.pos_x += -1
                self.pos_y += 0
                self.setPosition(self.pos_x, self.pos_y)
            
    #returns an ordered list of items in the player inventory
    def inventory(self):
        count_inventory = 1
        index = 0
        if len(self.player_inventory) > 0:
            for item in range(len(self.player_inventory)):
                if self.player_inventory[index].get_type_treasure() == "Gold":
                    return (str(count_inventory) + ". " + str(self.gold_amnt)
                            + " gold coins")#gold listed together
                else:
                    print(str(count_inventory) + ". " +
                          (self.player_inventory[index]).getName())
                    count_inventory += 1
                    index += 1
        else:
            return "You have no items in your inventory."
                      
    #adds items from the world to player inventory        
    def pickup(self, treasure_obj):
        index = 0
        goldAdded = False
        
        if treasure_obj.get_type_treasure() == "Gold":
            for item in self.player_inventory:
                if ((self.player_inventory[index]).get_type_treasure()
                    == "Gold"):
                    treasure_obj.pickup()
                    self.gold_amnt += treasure_obj.getQuantity()
                    goldAdded = True
                    print("You successfully picked up an item.")
                    break
                else:
                    index += 1
            if goldAdded == False:
                treasure_obj.pickup()
                self.player_inventory.append(treasure_obj)
                self.gold_amnt += treasure_obj.getQuantity()
                print("You successfully picked up gold.")          
        else:
            treasure_obj.pickup()
            self.player_inventory.append(treasure_obj)
            print("You successfully picked up an item.")

    #automatically equips armor and weapons accordingly
    def equip(self):
        if len(self.player_inventory) > 0:
            if len(self.equip_list) == 2:
                print("You are already wearing armor and wielding a weapon. "
                      "Please remove one to equip a new item.")
            elif len(self.equip_list) == 1:
                index = 0
                armorEquipped = False
                weaponEquipped = False
                if self.equip_list[0].get_type_treasure() == "Armor":
                    armorEquipped = True
                    for item in self.player_inventory:
                        if ((self.player_inventory[index]).get_type_treasure()
                            == "Weapon"):
                            self.player_inventory[index].wield()
                            self.equip_list.append(self.player_inventory[index])
                            self.attack += (
                                self.player_inventory[index]).getDamage()
                            weaponEquipped = True
                            print("You have successfully wielded a weapon.")
                            break
                        else:
                            index += 1
                    if weaponEquipped == False and armorEquipped == True:
                        print("You are already wearing armor and have no weapon"
                              " in your inventory to wield.")
                elif (self.equip_list[0]).get_type_treasure() == "Weapon":
                    weaponEquipped = True
                    for item in self.player_inventory:
                        if ((self.player_inventory[index]).get_type_treasure()
                            == "Armor"):
                            self.player_inventory[index].wear()
                            self.equip_list.append(self.player_inventory[index])
                            self.defense +=(
                                self.player_inventory[index]).getDefense()
                            armorEquipped = True
                            print("You have successfully equipped armor.")
                            break
                        else:
                            index += 1
                    if armorEquipped == False and weaponEquipped == True:
                        print("You are already wielding a weapon and have no "
                              "armor in your inventory to wear.")
            else:
                index = 0
                armorEquipped = False
                weaponEquipped = False
                for item in self.player_inventory:
                    if ((self.player_inventory[index]).get_type_treasure()
                        == "Weapon"):
                        self.player_inventory[index].wield()
                        self.equip_list.append(self.player_inventory[index])
                        self.attack += (
                            self.player_inventory[index]).getDamage()
                        weaponEquipped = True
                        print("You have successfully wielded a weapon.")
                        break
                    elif ((self.player_inventory[index]).get_type_treasure()
                          == "Armor"):
                        self.player_inventory[index].wear()
                        self.equip_list.append(self.player_inventory[index])
                        self.defense += (
                            self.player_inventory[index]).getDefense()
                        armorEquipped = True
                        print("You have successfully equipped armor.")
                        break
                    else:
                        index += 1
                if armorEquipped == False and weaponEquipped == False:
                    print("You have no weapons or armor in your inventory"
                          " to equip at this time.")
        else:
            print("You have no items in your inventory at this time.")

    #removes any armor the player is wearing
    def remove(self):
        if len(self.equip_list) > 0:
            if self.equip_list[0].get_type_treasure() == "Armor":
                self.equip_list[0].remove()
                self.defense -= self.equip_list[0].getDefense()
                self.player_inventory.remove(self.equip_list[0])
                self.player_inventory.append(self.equip_list[0])
                self.equip_list.remove(self.equip_list[0])
                print("You have successfully removed your armor.")

            elif self.equip_list[1].get_type_treasure() == "Armor":
                self.equip_list[1].remove()
                self.defense -= self.equip_list[1].getDefense()
                self.player_inventory.remove(self.equip_list[1])
                self.player_inventory.append(self.equip_list[1])
                self.equip_list.remove(self.equip_list[1])
                print("You have successfully removed your armor.")
        else:
            print("You have no armor to remove at this time.")

    #puts away the weapon the player is wielding
    def unwield(self):
        if len(self.equip_list) > 0:
            if self.equip_list[0].get_type_treasure() == "Weapon":
                self.equip_list[0].unwield()
                self.attack -= self.equip_list[0].getDamage()
                self.player_inventory.remove(self.equip_list[0])
                self.player_inventory.append(self.equip_list[0])
                self.equip_list.remove(self.equip_list[0])
                print("You have successfully unwielded your weapon.")

            elif self.equip_list[1].get_type_treasure() == "Weapon":
                self.equip_list[1].unwield()
                self.attack -= self.equip_list[1].getDamage()
                self.equip_list.remove(self.equip_list[1])
                self.player_inventory.remove(self.equip_list[1])
                self.player_inventory.append(self.equip_list[1])
                print("You have successfully unwielded your weapon.")
        else:
            print("You have no weapon to unwield at this time.")

    #eats a food item in the inventory
    def eat(self, index):
        if len(self.player_inventory) > 0:
            if index > 0 or index < len(self.player_inventory):
                if (self.player_inventory[
                    index - 1]).get_type_treasure() == "Food":
                    if self.health >= self.max_health:
                        self.health += (
                            self.player_inventory[index - 1]).getNutrition()
                        self.player_inventory.remove(
                            self.player_inventory[index - 1])
                        self.health -= 1
                        print("You have eaten too much, you lose 1 hp.")
                        #player loses hp if they eat food when they have maxhp
                    else:
                        self.health += self.player_inventory[
                            index - 1].getNutrition()
                        if self.health > self.max_health:
                            self.health = self.max_health
                        self.player_inventory.remove(
                            self.player_inventory[index - 1])
                        print("You have successfully eaten some food.")
                else:
                    print("The item you selected is not edible.")
            else:
                print("The number you typed is not a valid selection.")
        else:
            print("You have no items in your inventory to eat at this time.")

    #drops an item that is not being used by the player
    def drop(self, index):
        if len(self.player_inventory) > 0:
            if index > 0 or index < len(self.player_inventory):
                if ((self.player_inventory[index - 1]).get_type_treasure()
                    == "Armor"):
                    if self.player_inventory[index - 1].getWear() == True:
                        print("You are wearing this armor. You must remove it "
                              "before you can drop it.")
                    else:
                        (self.player_inventory[index-1]).setCarry(False)
                        location = (self.pos_x, self.pos_y)
                        (self.player_inventory[index-1]).drop(location)
                        self.player_inventory.remove(
                            self.player_inventory[index-1])
                        print("You have successfully dropped an item.")
                elif ((self.player_inventory[index - 1]).get_type_treasure()
                      == "Weapon"):
                    if self.player_inventory[index-1].getWield() == True:
                        print("You are wielding this weapon. You must unwield "
                              "it before you can drop it.")
                    else:
                        (self.player_inventory[index-1]).setCarry(False)
                        location = (self.pos_x, self.pos_y)
                        (self.player_inventory[index-1]).drop(location)
                        self.player_inventory.remove(
                            self.player_inventory[index-1])
                        print("You have successfully dropped an item.")
                elif ((self.player_inventory[index-1]).get_type_treasure()
                      == "Food"):
                    (self.player_inventory[index - 1]).setCarry(False)
                    location = (self.pos_x, self.pos_y)
                    (self.player_inventory[index - 1]).drop(location)
                    self.player_inventory.remove(
                        self.player_inventory[index-1])
                    print("You have successfully dropped an item.")
                elif ((self.player_inventory[index-1]).get_type_treasure()
                       == "Gold"):
                    (self.player_inventory[index-1]).setCarry(False)
                    dropped_amnt = self.gold_amnt
                    self.gold_amnt = 0
                    location = (self.pos_x, self.pos_y)
                    (self.player_inventory[index - 1]).drop(location)
                    self.player_inventory.remove(
                        self.player_inventory[index-1])
                    print("You have successfully dropped an item.")
            else:
                print("The number you typed is not a valid selection.")
        else:
            print("You have no items in your inventory to drop at this time.")
    
    
