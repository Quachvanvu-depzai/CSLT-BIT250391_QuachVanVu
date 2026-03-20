class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return f"Hoa {self.ten} có màu {self.mau}"
hoa_hong = Hoa("Hồng", "Đỏ thắm")
print(hoa_hong)
print()