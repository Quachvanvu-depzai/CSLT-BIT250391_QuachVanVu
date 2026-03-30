class Flower:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

flower = Flower("đỏ")
print(flower.get_color())
flower.set_color("vàng")
print(flower.get_color())