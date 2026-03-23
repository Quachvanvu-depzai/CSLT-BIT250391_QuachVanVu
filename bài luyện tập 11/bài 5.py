my_dict = {
    "ten": "Quách Văn Vũ",
    "tuoi": 20,
    "nganh_hoc": "Công nghệ thông tin",
    "diem_tb":5
}

def kiem_tra_key(tu_dien, key_can_tim):
    if key_can_tim in tu_dien:
        print(f"Key '{key_can_tim}' CÓ tồn tại. Giá trị của nó là: {tu_dien[key_can_tim]}")
    else:
        print(f"Key '{key_can_tim}' KHÔNG tồn tại trong dictionary.")
print("Danh sách dictionary hiện tại:", my_dict)
print("-" * 40)
kiem_tra_key(my_dict, "tuoi")
kiem_tra_key(my_dict, "diem_tb")
kiem_tra_key(my_dict, "so_thich")
