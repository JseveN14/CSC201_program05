#Jessica Neves
#treasure class
class Treasure(object):
    def __init__(self):
        self.name = "treasure"
        self.value = 0
        self.type_treasure = "Treasure"
        self.description = "a treasure item"
        pos_x = None
        pos_y = None
        self.position = (pos_x, pos_y)
        self.carry = False
        self.found = False

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def get_type_treasure(self):
        return self.type_treasure

    def lookat(self):
        return self.description

    def getPosition(self):
        return self.position

    def getCarry(self):
        return self.carry

    def getFound(self):
        return self.found

    def setValue(self, value):
        self.value += value

    def setPosition(self, pos_x, pos_y):
        self.position = (pos_x, pos_y)

    def setCarry(self, isCarried):
        self.carry = isCarried

    def setFound(self, isFound):
        self.found = isFound

    def pickup(self):
        self.position = None
        self.carry = True

    def drop(self, location):
        self.position = location
        self.carry = False
        self.found = False
        
#weapon, can be wielded, adds damage to player attack
class Weapon(Treasure):
    def __init__(self, name, value, description, damage):
        super().__init__()
        self.damage = damage
        self.name = name
        self.value = value
        self.description = description
        self.wielding = False
        self.type_treasure = "Weapon"

    def wield(self):
        self.wielding = True

    def unwield(self):
        self.wielding = False

    def getWield(self):
        return self.wielding

    def getDamage(self):
        return self.damage

#Armor, can be worn, adds defense to player defense
class Armor(Treasure):
    def __init__(self, name, value, description, defense):
        super().__init__()
        self.defense = defense
        self.name = name
        self.value = value
        self.description = description
        self.wearing = False
        self.type_treasure = "Armor"

    def wear(self):
        self.wearing = True

    def remove(self):
        self.wearing = False

    def getDefense(self):
        return self.defense

    def getWear(self):
        return self.wearing

#Food item, can be eaten, adds nutrition to player health
class Food(Treasure):
    def __init__(self, name, value, description, nutrition):
        super().__init__()
        self.nutrition = nutrition
        self.name = name
        self.type_treasure = "Food"
        self.description = description
        self.value = value
        self.eaten = False

    def eat(self):
        self.nutrition = 0
        self.eaten = True

    def getEaten(self):
        return self.eaten

    def getNutrition(self):
        return self.nutrition

#gold item, can be picked up, added to player's inventory with other gold
class Gold(Treasure):
    def __init__(self, name, description, quantity):
        super().__init__()
        self.name = name
        self.value = 1
        self.description = description
        self.type_treasure = "Gold"
        self.quantity = quantity

    def getQuantity(self):
        return self.quantity
        
