class SanPham:
    ten_cua_hang = "Siêu thị Python"
    def __init__(self, ma_sp, ten_sp, gia_ban):
        if not ma_sp:
            raise ValueError("Lỗi: Mã sản phẩm không được để trống!")
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.gia_ban = gia_ban
    @property
    def gia_ban(self):
        return self._gia_ban
    @gia_ban.setter
    def gia_ban(self, gia_tri):
        if gia_tri < 0:
            raise ValueError("Lỗi: Giá bán không thể là số âm!")
        self._gia_ban = gia_tri
    def __str__(self):
        return f"[{self.ma_sp}] {self.ten_sp} - Giá: {self.gia_ban:,.0f}đ"
    def tinh_thue_vat(self):
        return self.gia_ban * 0.1  # VAT 10%
    @classmethod
    def doi_ten_cua_hang(cls, ten_moi):
        cls.ten_cua_hang = ten_moi
    @staticmethod
    def la_gio_mo_cua(gio):
        return 8 <= gio <= 22
    def __eq__(self, other):
        if isinstance(other, SanPham):
            return self.ma_sp == other.ma_sp
        return False
class SanPhamKhuyenMai(SanPham):
    def __init__(self, ma_sp, ten_sp, gia_ban, ti_le_giam):
        # Gọi constructor của lớp cha
        super().__init__(ma_sp, ten_sp, gia_ban)
        self.ti_le_giam = ti_le_giam  # Ví dụ: 0.2 là giảm 20%

    def __str__(self):
        gia_sau_giam = self.gia_ban * (1 - self.ti_le_giam)
        return super().__str__() + f" -> Giảm còn: {gia_sau_giam:,.0f}đ (Sale {self.ti_le_giam * 100}%)"
print("--- 1. KHỞI TẠO VÀ IN ĐỐI TƯỢNG (__str__) ---")
sp1 = SanPham("SP01", "Bàn phím cơ", 1000000)
sp2 = SanPhamKhuyenMai("SP02", "Chuột không dây", 500000, 0.2)
print(sp1)
print(sp2)

print("\n--- 2. THỬ NGHIỆM GETTER / SETTER ---")
sp1.gia_ban = 1200000
print(f"Giá mới của {sp1.ten_sp} (qua Getter): {sp1.gia_ban:,.0f}đ")

print("\n--- 3. PHƯƠNG THỨC ĐỐI TƯỢNG ---")
print(f"Thuế VAT của {sp1.ten_sp}: {sp1.tinh_thue_vat():,.0f}đ")

print("\n--- 4. PHƯƠNG THỨC LỚP ---")
SanPham.doi_ten_cua_hang("Cửa hàng TechPro")
print(f"Cửa hàng hiện tại: {SanPham.ten_cua_hang}")

print("\n--- 5. PHƯƠNG THỨC TĨNH ---")
gio_hien_tai = 23
print(f"{gio_hien_tai}h cửa hàng có mở cửa không? -> {SanPham.la_gio_mo_cua(gio_hien_tai)}")

print("\n--- 6. NẠP CHỒNG TOÁN TỬ == ---")
sp_trung_ma = SanPham("SP01", "Bàn phím giả cơ", 300000)
print(f"sp1 có cùng mã sản phẩm với sp_trung_ma không? -> {sp1 == sp_trung_ma}")

print("\n--- 7. THỬ NGHIỆM BẮT LỖI (Xác thực ValueError) ---")

try:
    SanPham("", "Lỗi rỗng", 100000)
except ValueError as e:
    print(e)

try:
    sp1.gia_ban = -50000
except ValueError as e:
    print(e)