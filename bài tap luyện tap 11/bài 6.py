danh_sach_nguoi = {}
print("--- CHƯƠNG TRÌNH NHẬP VÀ TÍNH TUỔI TRUNG BÌNH ---")
print("(Gõ 'stop' hoặc 'dung' ở phần nhập tên để kết thúc)\n")
while True:
    ten = input("Nhập tên: ")
    if ten.lower() in ['stop', 'dung']:
        break
    try:
        tuoi = int(input(f"Nhập tuổi của {ten}: "))
        danh_sach_nguoi[ten] = tuoi
        print(f"Đã thêm: {ten} - {tuoi} tuổi.\n")
    except ValueError:
        print("Lỗi: Tuổi phải là một số nguyên. Vui lòng nhập lại!\n")
print("-" * 40)
if danh_sach_nguoi:
    print(f"Danh sách thông tin đã nhập: {danh_sach_nguoi}")
    tong_tuoi = sum(danh_sach_nguoi.values())
    so_luong = len(danh_sach_nguoi)
    tuoi_trung_binh = tong_tuoi / so_luong
    print(f"✅ Tuổi trung bình của {so_luong} người là: {tuoi_trung_binh:.2f}")
else:
    print("Bạn chưa nhập thông tin nào!")