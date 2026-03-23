class Student:
    def __init__(self, ten, diem):
        self.ten = ten

        if 0 <= diem <= 10:
            self.diem = diem
        else:
            raise ValueError("Điểm phải nằm trong khoảng 0–10")

    def display(self):
        print(f"Sinh viên {self.ten} có điểm là {self.diem}")

hoc_sinh1 = Student("Tú", 1)
hoc_sinh2 = Student("Vinh", 9)

hoc_sinh1.display()
hoc_sinh2.display()
