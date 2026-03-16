can_nang =  float(input("nhập cân nặng kg:"))
chieu_cao =  float(input("nhập chiều cao m:"))
def tinh_BMI():
    BMI = can_nang / (chieu_cao * chieu_cao)
    round(BMI, 1)
    print(chieu_cao)
    print(can_nang)
    print(round(BMI, 2))
tinh_BMI()