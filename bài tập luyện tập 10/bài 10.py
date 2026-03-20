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