def nhap_ma_tran(hang, cot, ten):
    ma_tran = []
    print(f"Nhập ma trận {ten}:")
    for i in range(hang):
        dong = []
        for j in range(cot):
            while True:
                gia_tri = input(f"Phần tử [{i}][{j}]: ")

                if gia_tri.strip() == "":
                    print("Lỗi: Không được để trống! Vui lòng nhập lại.")
                    continue

                try:
                    dong.append(float(gia_tri))
                    break
                except ValueError:
                    print("Lỗi: Phải nhập số! Vui lòng nhập lại.")
        ma_tran.append(dong)
    return ma_tran
def cong_ma_tran(A, B, hang, cot):
    C = []
    for i in range(hang):
        dong = []
        for j in range(cot):
            dong.append(A[i][j] + B[i][j])
        C.append(dong)
    return C
def in_ma_tran(M):
    for dong in M:
        print("\t".join(map(str, dong)))
while True:
    try:
        hang = int(input("Nhập số hàng: "))
        cot = int(input("Nhập số cột: "))
        break
    except ValueError:
        print("Lỗi: Phải nhập số nguyên!")
A = nhap_ma_tran(hang, cot, "A")
B = nhap_ma_tran(hang, cot, "B")
C = cong_ma_tran(A, B, hang, cot)
print("\nma trận A là : ")
in_ma_tran(A)
print("\nma trận B là : ")
in_ma_tran(B)
print("\nMa trận tổng:")
in_ma_tran(C)