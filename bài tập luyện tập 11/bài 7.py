import csv
def main():
    print("--- NHẬP THÔNG TIN NHÂN VIÊN ---")
    ten = input("Nhập tên nhân viên: ")
    tuoi = input("Nhập tuổi: ")
    id_nv = input("Nhập ID nhân viên: ")
    txt_filename = "nhan_vien.txt"
    csv_filename = "nhan_vien.csv"
    with open(txt_filename, "w", encoding="utf-8") as f_txt:
        f_txt.write(f"ID: {id_nv} | Tên: {ten} | Tuổi: {tuoi}")
    print(f"Đã lưu thành công vào: {txt_filename}")
    with open(csv_filename, "w", newline='', encoding="utf-8-sig") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["ID", "Tên", "Tuổi"])
        writer.writerow([id_nv, ten, tuoi])
    print(f"Đã lưu thành công vào: {csv_filename}")
    print("--- XEM TRƯỚC NỘI DUNG FILE TEXT ---")
    with open(txt_filename, "r", encoding="utf-8") as f_txt:
        print(f_txt.read())
    print("--- XEM TRƯỚC NỘI DUNG FILE CSV ---")
    with open(csv_filename, "r", encoding="utf-8") as f_csv:
        print(f_csv.read())
main()