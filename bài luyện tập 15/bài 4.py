a = float(input("điểm môn 1"))
b = float(input("điểm môn 2"))
c = float(input("điểm môn 3"))
diem_tb = (a+b+c)/3
print (diem_tb)
if diem_tb >=8:
    print("xép loại giỏi")
elif diem_tb >=6.5 or diem_tb <=7.9:
    print("xép loại khá")
elif diem_tb >= 5 or diem_tb <=6.4:
    print("xép loại trung bình")
elif diem_tb <5:
    print("xép loại yếu")