class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
    def __eq__(self, sv_khac):
        if isinstance(sv_khac, SinhVien):
            return self.diem == sv_khac.diem
        return False

sv1 = SinhVien("Nguyen Van A", 10.0)
sv2 = SinhVien("Le Thi B", 8.6)
sv3 = SinhVien("Tran Van C", 8.6)
print("--- Thông tin sinh viên ---")
print(f"{sv1.ten}: {sv1.diem} điểm")
print(f"{sv2.ten}: {sv2.diem} điểm")
print(f"{sv3.ten}: {sv3.diem} điểm")
print("\n--- Kết quả so sánh ---")

if sv1 == sv2:
    print(f"{sv1.ten} và {sv2.ten} có điểm BẰNG nhau.")
else:
    print(f"{sv1.ten} và {sv2.ten} có điểm KHÁC nhau.")
if sv1 == sv3:
    print(f"{sv1.ten} và {sv3.ten} có điểm BẰNG nhau.")
else:
    print(f"{sv1.ten} và {sv3.ten} có điểm KHÁC nhau.")