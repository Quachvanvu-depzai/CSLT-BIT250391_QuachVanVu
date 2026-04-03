danh_sach =[]
for i in range (1,6):
    ten = input("nhập tên:")
    danh_sach.append(ten)
    print(danh_sach)
danh_sach.pop(1)
print (f"danh sách khi xóa phần tử thứ 2 là :{danh_sach}")