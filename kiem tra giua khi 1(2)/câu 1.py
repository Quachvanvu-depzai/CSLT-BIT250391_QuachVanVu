so = float(input("nhap so"))
if so >= 0:
    phan_du=so%2
    print(phan_du)
else :
    raise ValueError("phải nhập số lớn hơn 0")