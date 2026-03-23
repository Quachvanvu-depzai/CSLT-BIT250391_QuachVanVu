a = int(input('nhập a:'))
def bang_cuu_chuong():
    if a <= 9 & a >0:
        for i in range (1,11):
            ket_qua=a*i
            print (ket_qua)
    else :
        print ('error')
print("bảng cửu chương")
bang_cuu_chuong()