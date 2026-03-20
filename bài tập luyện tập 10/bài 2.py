chuoi = input(" nhập chuỗi :")
chuoi_nhap = input("nhập ký tự :")
dem_ky_tu=0
for ch in chuoi:
    if ch == chuoi_nhap:
        dem_ky_tu += 1
print("Kí tự",chuoi_nhap,"xuất hiên",dem_ky_tu,"lần")
