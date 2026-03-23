a = float(input("nhập a:"))
b = float(input("nhập b:"))
def luy_thua(a, b):
    return a ** b, b ** a
def can_bac_2(a, b):
    return a ** (1/2) ,b ** (1/2)
def chia_lay_phan_nguyen(a, b):
    return a//b,b//a
def chia_lay_phan_du(a, b):
    return a%b ,b%a
def lam_tron(a,b):
    return round(a,0),round(b,0)
print("lũy thừa: ",luy_thua(a,b))
print("căn bậc 2:",can_bac_2(a,b))
print("chia lấy phần nguyên:",chia_lay_phan_nguyen(a,b))
print("làm tròn:",lam_tron(a,b))