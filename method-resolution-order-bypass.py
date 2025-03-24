from math import sin, pi


def deg_to_rad(deg: int):
    return deg * (pi / 180)


class Quadrangle:
    def __init__(self, sides: list[int], angles: list[int]):
        self.sides = sides
        self.angles = angles
        if not hasattr(self, "properties"):
            self.properties = {}

    def print_props(self):
        if len(self.properties) > 0:
            for prop in self.properties:
                print(prop)
        else:
            print("Нет свойств")


class Paralelogram(Quadrangle):
    def __init__(self, side_a: int, side_b: int, angle_a: int, angle_b: int, *args):
        if angle_a + angle_b != 180:
            raise ValueError('Углы должны попарно давать 180 градусов')

        super().__init__(
            sides=[
                side_a,
                side_b,
                side_a,
                side_b
            ],
            angles = [
                angle_a,
                angle_b,
                angle_a,
                angle_b
            ]
        )
        self.name = 'Параллелограм'
        self.properties[self.name] = [
            "Противоположные стороны попарно равны и параллельны", 
            "Противоположные углы попарно равны",
            "Углы, прилежащие к одной стороне, попарно дают 180 градусов"
        ]

    def area(self):
        return self.sides[0] * self.sides[1] * sin(deg_to_rad(self.angles[0]))


class Rectangle(Paralelogram):
    def __init__(self, side_a: int, side_b: int):
        Paralelogram.__init__(self, side_a, side_b, 90, 90)
        
        self.name = 'Прямоугольник'
        self.properties[self.name] = ["Все углы равны 90 градусов"]

    def area(self):
        return self.sides[0] * self.sides[1]


class Rhombus(Paralelogram):
    def __init__(self, side: int, angle_a: int, angle_b: int):
        Paralelogram.__init__(self, side, side, angle_a, angle_b)
        
        self.name = 'Ромб'
        self.properties[self.name] = ["Все стороны равны"]


class Square(Rectangle, Rhombus):
    def __init__(self, side: int):
        Rectangle.__init__(self, side, side)
        Rhombus.__init__(self, side, self.angles[0], self.angles[1])
        self.name = 'Квадрат'


bruh_1 = Paralelogram(12, 13, 60, 120)
bruh_2 = Rectangle(12, 13)
bruh_3 = Rhombus(5, 60, 120)
bruh_4 = Square(10)

bruhs = [bruh_1, bruh_2, bruh_3, bruh_4]
for i, bruh in enumerate(bruhs):
    properties_str = []
    for type in bruh.properties.keys():
        properties_str.append(f"{type}: {'. '.join(bruh.properties[type])}")
    print(f"{i}. {bruh.name} Свойства: \n{'\n'.join(properties_str)}")