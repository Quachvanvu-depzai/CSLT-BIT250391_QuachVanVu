m=int(input("nhập m:"))
n=int(input("nhập n:"))
hang=int(input("nhập hàng:"))
cot=int(input("nhập cột:"))
import numpy as np
matrix = np.random.randint(1,10,size=(m, n))
print(matrix)
if hang > m :
    print("tìm hàng lỗi")
else :
    print("hàng", hang, "là", matrix[hang - 1])
if cot > n :
    print ("tìm cột lỗi")
else:
    print("hàng", cot, "là", matrix[:, cot - 1])
print("Giá trị lớn nhất:", np.max(matrix))