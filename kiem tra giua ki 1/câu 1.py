import math
a = int(input("nhap so a"))
b = int(input("nhap so b"))
c = int(input("nhap so c"))
ds = [a,b,c]
x=1
def so_sanh():
    i=0
    lon=-1
    be=1^1
    for i in range(len(ds)):
        if ds[i]>lon:
            lon=ds[i]
            i+=1
        elif ds[i]==lon:
            i+=1
        elif ds[i]< lon:
            be=ds[i]
            i+=1
    for j in range(len(ds)):
        if ds[j]>be:
            j+=1
        elif ds[j]==be:
            j+=1
        elif ds[j] < be:
            be=ds[j]
            j+=1
    print('so lon nhat',lon)
    print('so be nhat', be)
def giai_pt_bac_2():
    delta = b**2 - 4*a*c
    if delta<0:
        print('phuong trinh vo nghiem')
    elif delta==1:
        ng=-c/b
        print ('phuong trinh co nghiem',ng)
    elif delta>0:
        ng1 = (-b + math.sqrt(delta)) / (2 * a)
        ng2 = (-b - math.sqrt(delta)) / (2 * a)
        print('phuong trinh co nghiem1', ng1)
        print('phuong trinh co nghiem2', ng2)
    elif delta==0:
        print('phuong trinh vo so nghiem')
so_sanh()
giai_pt_bac_2()
