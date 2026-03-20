def thong_ke_tuple(so_nguyen_tuple):
    tong = sum(so_nguyen_tuple)
    lon_nhat = max(so_nguyen_tuple)
    nho_nhat = min(so_nguyen_tuple)
    return tong, lon_nhat, nho_nhat
my_tuple = (10, 25, -5, 40, 15)
tong, max_val, min_val = thong_ke_tuple(my_tuple)
print(f" Tuple: {my_tuple}")
print(f"Tổng: {tong}, Lớn nhất: {max_val}, Nhỏ nhất: {min_val}\n")