chuoi_dau_vao = input("Nhập vào một chuỗi bất kỳ: ")
def thong_ke_chuoi(chuoi):
    in_hoa = 0
    in_thuong = 0
    chu_so = 0
    ky_tu_dac_biet = 0
    khoang_trang = 0
    nguyen_am = 0
    phu_am = 0
    tap_nguyen_am = "aeiouAEIOU"
    for char in chuoi:
        if char.isspace():
            khoang_trang += 1
        elif char.isdigit():
            chu_so += 1
        elif char.isalpha():
            if char.isupper():
                in_hoa += 1
            else:
                in_thuong += 1
            if char in tap_nguyen_am:
                nguyen_am += 1
            else:
                phu_am += 1
        else:
            ky_tu_dac_biet += 1
    print("\n--- KẾT QUẢ THỐNG KÊ ---")
    print(f"- Số lượng chữ cái in hoa: {in_hoa}")
    print(f"- Số lượng chữ cái in thường: {in_thuong}")
    print(f"- Số lượng chữ số: {chu_so}")
    print(f"- Số lượng ký tự đặc biệt: {ky_tu_dac_biet}")
    print(f"- Số lượng ký tự khoảng trắng: {khoang_trang}")
    print(f"- Số lượng nguyên âm: {nguyen_am}")
    print(f"- Số lượng phụ âm: {phu_am}")
thong_ke_chuoi(chuoi_dau_vao)