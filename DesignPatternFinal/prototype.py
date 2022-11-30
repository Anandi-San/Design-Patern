from abc import ABC, abstractmethod
import copy

class bulletPrototype(ABC):
    def __init__(self):
        self.coordinateX = None
        self.coordinateY = None
        self.damage = None
        self.speed = None

    @abstractmethod
    def clone(self):
        pass

class newBullet(bulletPrototype):
    def __init__(self, coordinateX, coordinateY, damage, speed):
        super().__init__()

        self.coordinateX = coordinateX
        self.coordinateY = coordinateY
        self.damage = damage
        self.speed = speed

    def __str__(self):
        return f"A new bullet will be created at coordinate ({self.coordinateX},{self.coordinateY}) with a damage value of {self.speed} and speed value of {self.damage}"

    def clone(self):
        return copy.deepcopy(self)

if __name__ == '__main__':
    createbullet = newBullet(500, 300, 100, 5)
    print(createbullet)