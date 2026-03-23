s = input("Nhập chuỗi số: ")
numbers = [int(x.strip()) for x in s.split(";")]
print("Các số:")
for n in numbers:
    print(n)
so_chan = sum(1 for n in numbers if n % 2 == 0)
so_le = sum(1 for n in numbers if n < 0)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
so_nguyen_to = sum(1 for n in numbers if is_prime(n))
gia_tri_tb = sum(numbers) / len(numbers)
print("Số chẵn:", so_chan)
print("Số âm:", so_le)
print("Số nguyên tố:", so_nguyen_to)
print("Giá trị trung bình:", gia_tri_tb)