def dao_nguoc_chuoi():
    chuoi = input("Nhập vào một chuỗi cần đảo ngược: ")
    chuoi_nguoc = ""
    for ky_tu in chuoi:
        chuoi_nguoc = ky_tu + chuoi_nguoc
    print("Chuỗi sau khi đảo ngược là:",chuoi_nguoc)
dao_nguoc_chuoi()