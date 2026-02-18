from crosshair import Crosshair
from weapon import Weapon, m4a4, ak47

class Player:

    def __init__(self, x, y, health, weapon):
        self.x = x
        self.y = y
        self.health = health
        self.crosshair = Crosshair(x, y)
        self.weapon = weapon

    def step(self, direction:str):
        if direction == "right":
            self.x += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "forward":
            self.y += 1
        elif direction == "backwards":
            self.y -= 1

    def take_damage(self, damage:int):
        self.health -= damage


        
        