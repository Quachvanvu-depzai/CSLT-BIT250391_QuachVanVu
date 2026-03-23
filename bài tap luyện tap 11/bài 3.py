ds_so = [1,4,2,6,9,8,7,99,26,2,4,19,0,8]
print(ds_so)
def tim_so_chan():
    tong = 0
    print("có số chẵn trong danh sách là : ")
    for i in ds_so:
        if i % 2 == 0:
            print(i)
            tong+=i
    print("tổng của các số chẵn là : ",tong)
tim_so_chan()