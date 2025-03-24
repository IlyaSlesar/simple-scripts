from math import sin, pi


def deg_to_rad(deg: int):
    return deg * (pi / 180)


class Quadrangle:
    def __init__(self, sides: list[int], angles: list[int]):
        self.name = 'Четырёхсторонняя фигура'
        self.sides = sides
        self.angles = angles
        self.properties = {}

    def props_str(self):
        if len(self.properties) > 0:
            properties_str = []
            for type in self.properties.keys():
                properties_str.append(f"{type}: {'. '.join(self.properties[type])}")
        else:
            properties_str = ['Нет свойств']

        return properties_str


class Paralelogram(Quadrangle):
    def __init__(self, sides: list[int], angles: list[int]):
        angles_n = len(angles)
        if not all(
                angles[i] + angles[(i + 1) % angles_n] == 180
                for i in range(angles_n)
            ):
            raise ValueError('Углы должны попарно давать 180 градусов')
        if not (sides[0] == sides[2] and sides[1] == sides[3]):
            raise ValueError('Стороны должны быть попарно равны')

        super().__init__(sides, angles)
        
        self.name = 'Параллелограмм'
        self.properties[self.name] = [
            "Противоположные стороны попарно равны и параллельны", 
            "Противоположные углы попарно равны",
            "Углы, прилежащие к одной стороне, попарно дают 180 градусов"
        ]

    def area(self):
        return self.sides[0] * self.sides[1] * sin(deg_to_rad(self.angles[0]))
    
    @classmethod
    def create(cls, side_a, side_b, angle_a, angle_b):
        return cls(
            sides=[side_a, side_b] * 2,
            angles=[angle_a, angle_b] * 2
        )


class Rectangle(Paralelogram):
    def __init__(self, sides: list[int], angles: list[int]):
        if not all(angle == 90 for angle in angles):
            raise ValueError('Углы должны быть равны 90')
        
        super().__init__(sides, angles)
        
        self.name = 'Прямоугольник'
        self.properties[self.name] = ["Все углы равны 90 градусов"]

    def area(self):
        return self.sides[0] * self.sides[1]
    
    @classmethod
    def create(cls, side_a, side_b):
        return cls(
            sides=[side_a, side_b] * 2,
            angles=[90] * 4
        )


class Rhombus(Paralelogram):
    def __init__(self, sides: list[int], angles: list[int]):
        super().__init__(sides, angles)
        
        self.name = 'Ромб'
        self.properties[self.name] = ["Все стороны равны"]

    @classmethod
    def create(cls, side, angle_a, angle_b):
        return cls(
            sides=[side] * 4,
            angles=[angle_a, angle_b] * 2
        )


class Square(Rectangle, Rhombus):
    def __init__(self, sides: list[int], angles: list[int]):
        super().__init__(sides, angles)
        
        self.name = 'Квадрат'

    @classmethod
    def create(cls, side):
        return cls(
            sides=[side] * 4,
            angles=[90] * 4
        )


bruh_1 = Paralelogram.create(12, 13, 60, 120)
bruh_2 = Rectangle.create(12, 13)
bruh_3 = Rhombus.create(5, 60, 120)
bruh_4 = Square.create(10)

bruhs = [bruh_1, bruh_2, bruh_3, bruh_4]
for i, bruh in enumerate(bruhs, start=1):
    print(f'{i}. Свойства {bruh.name}:\n{"\n".join(bruh.props_str())}')
    