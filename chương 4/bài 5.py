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
            raise ValueError("Lỗi: Giá sản phẩm (price) bắt buộc phải lớn hơn 0!")

    def __str__(self):
        return f"Thông tin sản phẩm: Giá = {self._price} VNĐ"
sp1 = Product(900)
print(sp1)
sp1.price = 200000
print("Sau khi cập nhật giá hợp lệ:", sp1)