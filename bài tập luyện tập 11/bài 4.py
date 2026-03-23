def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
danh_sach = [5, 12, 7, 5, 2, 19, 8]
print(f"Danh sách ban đầu: {danh_sach}")
phan_tu_moi = int(input("nhập phần tử mới thêm vào : "))
danh_sach.append(phan_tu_moi)
print(f"Danh sách sau khi thêm {phan_tu_moi}: {danh_sach}")
try:
    k = int(input("\nNhập giá trị k cần đếm: "))
    so_lan = danh_sach.count(k)
    print(f"Số {k} xuất hiện {so_lan} lần trong danh sách.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")
tong_nguyen_to = sum(so for so in danh_sach if kiem_tra_nguyen_to(so))
print(f"\nTổng các số nguyên tố trong danh sách là: {tong_nguyen_to}")
danh_sach.sort()
print(f"Danh sách sau khi sắp xếp tăng dần: {danh_sach}")
danh_sach.clear()
print(f"Danh sách sau khi xóa: {danh_sach}")
