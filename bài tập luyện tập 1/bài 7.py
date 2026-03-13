class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

hoc_sinh1 = Student("Tú", 8.5)
hoc_sinh2 = Student("Vinh", 9.0)

print("Sinh viên 1:", hoc_sinh1.ten, "-", hoc_sinh1.diem)
print("Sinh viên 2:", hoc_sinh2.ten, "-", hoc_sinh2.diem)