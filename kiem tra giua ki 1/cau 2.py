def in17_111():
    for i in range(17,112,1):
        if i%2==1:
            print(i)
def tim_so_nguyen_to():
    for i in range(17,112,1):
        if i%2==1 & i%3==1 & i%4==1 & i%5==1:
            print('cac so nguyen to',i)
in17_111()
tim_so_nguyen_to()


