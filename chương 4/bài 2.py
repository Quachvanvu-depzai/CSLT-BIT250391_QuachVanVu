def tinh_diem_trung_binh(danh_sach_sv):
    if not danh_sach_sv:
        return 0
    tong_diem = sum(danh_sach_sv.values())
    so_luong_sv = len(danh_sach_sv)
    return tong_diem / so_luong_sv
sinh_vien = {"An": 8.5, "Bình": 9.0, "Châu": 7.5}
diem_tb = tinh_diem_trung_binh(sinh_vien)
print("Danh sách điểm:", sinh_vien)
print(f"Điểm trung bình của lớp: {diem_tb:.2f}\n")