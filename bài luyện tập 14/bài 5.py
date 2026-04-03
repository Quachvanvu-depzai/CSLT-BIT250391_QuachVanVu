class Book:
    def __init__(self, name="", price=0):
        self.__name = name
        self.__price = price
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_price(self):
        return self.__price
    def set_price(self, price):
        if price < 0:
            self.__price = 0
        else:
            self.__price = price
my_book = Book()
my_book.set_name("Sách Giáo Khoa")
my_book.set_price(25000)
print(f"Giá của đối tượng vừa tạo là: {my_book.get_price()}")
books = [
    Book("Book 1", 30000),
    Book("Book 2", 50000),
    Book("Book 3", 100000)
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