class SinhVien:
    so_luong_sv = 0
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
        SinhVien.so_luong_sv += 1
    def __eq__(self, sv_khac):
        if isinstance(sv_khac, SinhVien):
            return self.diem == sv_khac.diem
        return False
    @classmethod
    def lay_tong_so_luong(cls):
        return cls.so_luong_sv
print(f"Số lượng ban đầu: {SinhVien.lay_tong_so_luong()}")
sv1 = SinhVien("Nguyen Van A", 10.0)
sv2 = SinhVien("Le Thi B", 7.0)
sv3 = SinhVien("Tran Van C", 7.5)
print(f"Đã tạo {sv1.ten}, {sv2.ten}, {sv3.ten}...")

tong = SinhVien.lay_tong_so_luong()
print(f"Tổng số sinh viên: {tong}")
