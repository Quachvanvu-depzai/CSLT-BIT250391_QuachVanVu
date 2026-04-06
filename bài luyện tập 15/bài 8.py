class Product:
    def __init__(self, price):
        self.price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Lỗi: Giá sản phẩm (price) không được nhỏ hơn 0!")
        self._price = value
sp_hop_le = Product(150000)
print(f"Đã tạo sản phẩm với giá: {sp_hop_le.price}")
