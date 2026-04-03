import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True
def chinh():
    nhap = input("Nhập mảng các số tự nhiên (cách nhau bởi khoảng trắng): ")
    arr = list(map(int, nhap.split()))
    odds = [x for x in arr if x % 2 != 0]
    count_odds = len(odds)
    primes = [x for x in arr if is_prime(x)]
    print(f"Các số lẻ: {' '.join(map(str, odds))} - Tổng số lượng: {count_odds}")
    print(f"Các số nguyên tố: {' '.join(map(str, primes))}")
chinh()