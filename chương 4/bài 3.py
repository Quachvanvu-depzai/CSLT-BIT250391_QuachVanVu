def kiem_tra_key(tu_dien, key_can_tim):
    if key_can_tim in tu_dien:
        print(f"Key '{key_can_tim}' CÓ tồn tại trong dictionary.")
    else:
        print(f"Key '{key_can_tim}' KHÔNG tồn tại trong dictionary.")
my_dict = {"name": "Python", "year": 1991, "creator": "Guido van Rossum"}
print(my_dict)
kiem_tra_key(my_dict, "name")
kiem_tra_key(my_dict, "version")
print()