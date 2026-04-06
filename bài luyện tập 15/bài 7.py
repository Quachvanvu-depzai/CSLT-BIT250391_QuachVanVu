def tinh_diem_trung_binh(dict_sinh_vien):
    if not dict_sinh_vien:
        return 0
    tong_diem = sum(dict_sinh_vien.values())
    so_luong = len(dict_sinh_vien)
    return tong_diem / so_luong
danh_sach_sinh_vien = {
    "Nguyễn văn nam": 8.5,
    "Trần Thị lê": 7.0,
    "Lê Văn quỳnh": 9.2
}
diem_tb = tinh_diem_trung_binh(danh_sach_sinh_vien)
print(f"Điểm trung bình của các sinh viên là: {diem_tb:.2f}")