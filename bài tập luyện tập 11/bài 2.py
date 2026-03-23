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
def binary_search_custom(arr, target):
    target_len = len(target)
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_len = len(arr[mid])
        if mid_len == target_len:
            if arr[mid] == target:
                return mid
            else:
                temp = mid - 1
                while temp >= left and len(arr[temp]) == target_len:
                    if arr[temp] == target: return temp
                    temp -= 1
                temp = mid + 1
                while temp <= right and len(arr[temp]) == target_len:
                    if arr[temp] == target: return temp
                    temp += 1
                return -1
        elif mid_len < target_len:
            right = mid - 1
        else:
            left = mid + 1
    return -1
#danh_sach_tu_bai_1 = ['chuoixyz', 'chuoi1', 'chuoi2', 'abc', 'ab']
print(f"Mảng hiện tại (đã sắp xếp theo độ dài giảm dần): {a}")
chuoi_can_tim = input("Nhập chuỗi bạn muốn tìm kiếm: ")
vi_tri = binary_search_custom(a, chuoi_can_tim)
if vi_tri != -1:
    print(f"-> Đã tìm thấy chuỗi '{chuoi_can_tim}' tại vị trí index: {vi_tri}")
else:
    print(f"-> Không tìm thấy chuỗi '{chuoi_can_tim}' trong danh sách.")