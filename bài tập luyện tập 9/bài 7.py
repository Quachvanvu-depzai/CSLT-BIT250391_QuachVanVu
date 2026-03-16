class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, data_string):
        name, age = data_string.split("-")
        return cls(name, int(age))
    def __str__(self):
        return f"Tên: {self.name}, Tuổi: {self.age}"
p1 = Person("Minh", 25)
print("Khởi tạo thường:", p1)