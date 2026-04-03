class Book():
    def __init__(self,name="",price=0):
        self._name = name
        self._price = price
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price
sach = Book()
sach.set_name("doraemon")
sach.set_price(120000)
print("Giá của quyển sách là:", sach.get_price())

