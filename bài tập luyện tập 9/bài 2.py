so = int(input("nhập số"))
ds_so = [int(d) for d in str(so)]
tong=0
for i in range(0,len(ds_so)):
     tong += int(ds_so[i])
print(tong)
