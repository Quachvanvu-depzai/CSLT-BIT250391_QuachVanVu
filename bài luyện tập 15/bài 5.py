def count_vowels(s):
    tap_nguyen_am = "aeiou"
    dem = 0
    for char in s.lower():
        if char in tap_nguyen_am:
            dem += 1
    return dem

chuoi_test = "Hoc Python that TuyeT VOI"
print(f"Số lượng nguyên âm trong chuỗi là: {count_vowels(chuoi_test)}")