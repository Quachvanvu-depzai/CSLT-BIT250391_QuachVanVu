class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Tiếng kêu của động vật")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f"{self.name} sủa: gou gou!")
my_dog = Dog("mic")
print(f"Tên chú chó: {my_dog.name}")
my_dog.sound()