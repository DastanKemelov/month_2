class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):3

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return 3.14159 * self.__radius ** 2

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area():.2f}{self.unit}.")


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 0.5 * self.__side_a * self.__side_b

    def info(self):
        print(f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, area: {self.calculate_area():.2f}{self.unit}.")


#объекты
circle1 = Circle(2)
circle2 = Circle(5)
triangle1 = RightTriangle(6, 7)
triangle2 = RightTriangle(6, 14)
triangle3 = RightTriangle(7, 15)

# Список объектов
figures_list = [circle1, circle2, triangle1, triangle2, triangle3]

# метод info
for figure in figures_list:
    figure.info()
