
ma_sp = input("Nhập mã sản phẩm: ")
ten = input("Nhập tên sản phẩm: ")
gia = float(input("Nhập giá: "))

with open("product.txt", "a", encoding="utf-8") as f:
    f.write(f"{ma_sp};{ten};{gia}\n")

print("Đã thêm sản phẩm vào tệp.")