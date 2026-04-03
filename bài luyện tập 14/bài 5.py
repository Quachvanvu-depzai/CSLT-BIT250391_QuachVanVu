class Book:
    def __init__(self, name="", price=0):
        self._name = name
        self._price = price
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_price(self):
        return self._price
    def set_price(self, price):
        if price < 0:
            self._price = 0
        else:
            self._price = price
books = [
    Book("doraemon", 30000),
    Book("conan", 50000),
    Book("novel", 100000)
]
file_txt = open("output_bai5.txt", "w", encoding="utf-8")
tong_tien = 0
for b in books:
    ten_sach = b.get_name()
    gia_sach = b.get_price()
    file_txt.write(ten_sach + ";" + str(gia_sach) + "\n")
    tong_tien += gia_sach
file_txt.write("Tong;" + str(tong_tien))
file_txt.close()
print("Đã tạo và ghi dữ liệu thành công vào file 'output_bai5.txt'!")