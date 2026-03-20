def lay_ten_co_duoi(duong_dan):
    duong_dan_chuan = duong_dan.replace('\\', '/')

    ten_file = duong_dan_chuan.split('/')[-1]
    return ten_file
def lay_ten_khong_duoi(duong_dan):
    ten_file = lay_ten_co_duoi(duong_dan)
    if '.' in ten_file:
        ten_khong_duoi = ten_file.rsplit('.', 1)[0]
        return ten_khong_duoi
    return ten_file
duong_dan_1 = "d:\\music\\muabui.mp3"
duong_dan_2 = "/Users/admin/Downloads/bai_hat.remix.wav"
print("Đường dẫn 1:", duong_dan_1)
print(" - Có đuôi:", lay_ten_co_duoi(duong_dan_1))
print(" - Không đuôi:", lay_ten_khong_duoi(duong_dan_1))
print("-" * 30)
print("Đường dẫn 2:", duong_dan_2)
print(" - Có đuôi:", lay_ten_co_duoi(duong_dan_2))
print(" - Không đuôi:", lay_ten_khong_duoi(duong_dan_2))