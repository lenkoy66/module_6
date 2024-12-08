#Они все так похожи
import math

class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides):
        self.__color = list(__color)
        self.filled = False
        if len(__sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(__sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(c , int) and 0 <= c <= 255 for c in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        return all(isinstance(a, int) for a in args) and len(args) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return len(self) / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius() ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p_2 = len(self) / 2
        s = math.sqrt(p_2 * (p_2 - sides[0]) * (p_2 - sides[1]) * (p_2 - sides[2]))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, __side):
        sides = [__side] * self.sides_count
        super().__init__(__color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle0 = Circle((200, 200, 100), 10, 15, 6)
print(circle0.get_sides())
trangle0 = Triangle((200, 200, 100), 10, 6)
print(trangle0.get_sides())
cube0 = Cube((200, 200, 100), 9)
print(cube0.get_sides())
cube2 = Cube((200, 200, 100), 12)
print(cube2.get_sides())

print("----------------------------------")
#проверка:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())