#Ошибка эволюции
import random

class Animal:
    sound = None
    _DEGREE_OF_DANGER = 0
    live = True

    def __init__(self, speed, _cords=None):
        if _cords is None:
            self._cords = [0, 0, 0]
        else:
            self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        x = self._cords[0] + dx * self.speed
        y = self._cords[1] + dy * self.speed
        z = self._cords[2] + dz * self.speed
        if dz < 0:
            print(f"It's too deep, i can't dive :(")
        else:
            self._cords = [x, y, z]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, i'm peaceful :)")
        else:
            print(f"Be careful, i'm attacking you 0_0")

    def speak(self):
        print(f'{self.sound}')


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f'Here are(is) {eggs} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        z = abs(dz) * (self.speed // 2)
        self._cords[2] -= z


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)




db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()