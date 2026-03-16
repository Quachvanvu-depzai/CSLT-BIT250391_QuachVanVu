class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Lỗi: Giá của sản phẩm phải lớn hơn 0!")

    def __str__(self):
        return f"Thông tin sản phẩm - Giá: {self.price} VNĐ"

san_pham = Product(150000)

print("--- KHỞI TẠO THÀNH CÔNG ---")
print(san_pham)

san_pham.price = 6000
print("\n--- SAU KHI CẬP NHẬT GIÁ ---")
print(san_pham)