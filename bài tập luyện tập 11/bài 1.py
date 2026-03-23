a = []
for i in range(5):
    s = input(f"Nhập chuỗi {i+1}: ")
    a.append(s)
for i in range(1, 5):
    key = a[i]
    j = i - 1
    while j >= 0 and len(a[j]) < len(key):
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
    print(f"Bước {i}: {a}")