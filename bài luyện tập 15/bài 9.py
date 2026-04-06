def luu_file_txt():
    chuoi_nhap = input("Nhập một chuỗi ký tự bất kỳ: ")
    with open("du_lieu_bai_9.txt", "w", encoding="utf-8") as file:
        file.write(chuoi_nhap)
    print("✅ Đã lưu chuỗi thành công vào file 'du_lieu_bai_9.txt'")
luu_file_txt()