# --- CÁC HÀM TRỐNG ĐỂ CHỨA CODE TỪ BÀI 1 ĐẾN BÀI 10 ---
# Bạn hãy dán code của từng bài tương ứng vào bên trong các hàm này
def bai_1():
    def lay_ten_co_duoi(duong_dan):
        duong_dan_chuan = duong_dan.replace('\\', '/')

        ten_file = duong_dan_chuan.split('/')[-1]
        return ten_file

    def lay_ten_khong_duoi(duong_dan):
        ten_file = lay_ten_co_duoi(duong_dan)
        if '.' in ten_file:
            ten_khong_duoi = ten_file.rsplit('.', 1)[0]
            return ten_khong_duoi
        return ten_file

    duong_dan_1 = "d:\\music\\muabui.mp3"
    duong_dan_2 = "/Users/admin/Downloads/bai_hat.remix.wav"
    print("Đường dẫn 1:", duong_dan_1)
    print(" - Có đuôi:", lay_ten_co_duoi(duong_dan_1))
    print(" - Không đuôi:", lay_ten_khong_duoi(duong_dan_1))
    print("-" * 30)
    print("Đường dẫn 2:", duong_dan_2)
    print(" - Có đuôi:", lay_ten_co_duoi(duong_dan_2))
    print(" - Không đuôi:", lay_ten_khong_duoi(duong_dan_2))
def bai_2():
    chuoi = input(" nhập chuỗi :")
    chuoi_nhap = input("nhập ký tự :")
    dem_ky_tu = 0
    for ch in chuoi:
        if ch == chuoi_nhap:
            dem_ky_tu += 1
    print("Kí tự", chuoi_nhap, "xuất hiên", dem_ky_tu, "lần")
def bai_3():
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
def bai_4():
    chuoi = input("nhập chuỗi : ")
    do_dai_chuoi = len(chuoi)
    if not chuoi:
        raise ValueError("chuỗi rỗng")
    else:
        print("độ dài của chuỗi là", do_dai_chuoi)
def bai_5():
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(0, 10, 100)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    y1 = x ** 2
    ax1.plot(x, y1, color='blue', linewidth=2)
    ax1.set_title('Đồ thị $y = x^2$', fontsize=14)
    ax1.set_xlabel('Trục X', fontsize=12)
    ax1.set_ylabel('Trục Y', fontsize=12)
    ax1.grid(True, linestyle='--', alpha=0.7)
    y2 = np.sqrt(x)
    ax2.plot(x, y2, color='green', linewidth=2)
    ax2.set_title('Đồ thị $y = \\sqrt{x}$', fontsize=14)
    ax2.set_xlabel('Trục X', fontsize=12)
    ax2.set_ylabel('Trục Y', fontsize=12)
    ax2.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
def bai_6():
    def dao_nguoc_chuoi():
        chuoi = input("Nhập vào một chuỗi cần đảo ngược: ")
        chuoi_nguoc = ""
        for ky_tu in chuoi:
            chuoi_nguoc = ky_tu + chuoi_nguoc
        print("Chuỗi sau khi đảo ngược là:", chuoi_nguoc)
    dao_nguoc_chuoi()
def bai_7():
    mat_khau = input("nhập mật khẩu")
    mat_khau_dung = "python123"
    while mat_khau == mat_khau_dung:
        break
    while mat_khau != mat_khau_dung:
        mat_khau = input("mật khẩu sai vui lòng nhập lại")
    print("mật khẩu đã nhập đúng")
def bai_8():
    def sap_xep_noi_bot_theo_do_dai():
        danh_sach = []
        print("Vui lòng nhập 5 chuỗi bất kỳ:")
        for i in range(5):
            chuoi = input(f"Nhập chuỗi thứ {i + 1}: ")
            danh_sach.append(chuoi)
        print("\n" + "=" * 40)
        print(f"Danh sách ban đầu: {danh_sach}")
        print("=" * 40 + "\n")
        n = len(danh_sach)
        for i in range(n - 1):
            print(f"--- Lượt chạy thứ {i + 1} ---")
            da_hoan_doi = False
            for j in range(0, n - i - 1):
                if len(danh_sach[j]) < len(danh_sach[j + 1]):
                    danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
                    da_hoan_doi = True
                    print(f"  Hoán đổi: '{danh_sach[j + 1]}' <-> '{danh_sach[j]}' => {danh_sach}")
                else:
                    print(f"  Giữ nguyên: '{danh_sach[j]}' và '{danh_sach[j + 1]}'")
            if not da_hoan_doi:
                print("  -> Không có sự hoán đổi nào xảy ra, danh sách đã sắp xếp xong!")
                break
        print("\n" + "=" * 40)
        print(f"Danh sách sau khi sắp xếp (giảm dần): {danh_sach}")
        print("=" * 40)
    sap_xep_noi_bot_theo_do_dai()
def bai_9():
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
def bai_10():
    def sap_xep_noi_bot_theo_do_dai():
        danh_sach = []
        print("Vui lòng nhập 5 chuỗi bất kỳ:")
        for i in range(5):
            chuoi = input(f"Nhập chuỗi thứ {i + 1}: ")
            danh_sach.append(chuoi)
        print("\n" + "=" * 40)
        print(f"Danh sách ban đầu: {danh_sach}")
        print("=" * 40 + "\n")
        n = len(danh_sach)
        for i in range(n - 1):
            print(f"--- Lượt chạy thứ {i + 1} ---")
            da_hoan_doi = False

            for j in range(0, n - i - 1):
                if len(danh_sach[j]) < len(danh_sach[j + 1]):
                    danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
                    da_hoan_doi = True
                    print(f"  Hoán đổi: '{danh_sach[j + 1]}' <-> '{danh_sach[j]}' => {danh_sach}")
                else:
                    print(f"  Giữ nguyên: '{danh_sach[j]}' và '{danh_sach[j + 1]}'")
            if not da_hoan_doi:
                print("  -> Không có sự hoán đổi nào xảy ra, danh sách đã sắp xếp xong!")
                break
        print("\n" + "=" * 40)
        print(f"Danh sách sau khi sắp xếp (giảm dần): {danh_sach}")
        print("=" * 40)
    sap_xep_noi_bot_theo_do_dai()
def chay_menu():
    danh_sach_bai_tap = {
        "1": bai_1, "2": bai_2, "3": bai_3, "4": bai_4, "5": bai_5,
        "6": bai_6, "7": bai_7, "8": bai_8, "9": bai_9, "10": bai_10
    }
    while True:
        print("\n" + "=" * 45)
        print("          MENU CHƯƠNG TRÌNH (1-10)          ")
        print("=" * 45)
        print(" - Nhập số từ 1 đến 10 để chạy bài tập tương ứng.")
        print(" - Nhập '0' để thoát chương trình.")
        print("-" * 45)
        lua_chon = input("Vui lòng nhập lựa chọn của bạn: ").strip()
        if lua_chon == "0":
            print("Đã thoát chương trình. Tạm biệt!")
            break
        elif lua_chon in danh_sach_bai_tap:
            danh_sach_bai_tap[lua_chon]()
            input("\n-> Nhấn Enter để quay lại Menu...")
        else:
            print("⚠ Lựa chọn không hợp lệ, vui lòng nhập lại!")
chay_menu()