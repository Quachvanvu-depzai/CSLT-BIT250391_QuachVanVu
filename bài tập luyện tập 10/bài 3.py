def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)
try:
    so_nhap = int(input("Vui lòng nhập vào một số nguyên dương: "))
    if so_nhap < 0:
        print("Lỗi: Không thể tính giai thừa cho số âm!")
    else:
        ket_qua = tinh_giai_thua(so_nhap)
        print(f"Giai thừa của {so_nhap} là: {ket_qua}")
except ValueError:
    print("Lỗi: Bạn phải nhập vào một số nguyên hợp lệ!")