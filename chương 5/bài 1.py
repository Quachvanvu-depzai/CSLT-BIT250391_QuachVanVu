import matplotlib.pyplot as plt
xep_loai = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
so_luong = [6, 10, 12, 4, 1]
plt.bar(xep_loai, so_luong, color='skyblue', edgecolor='black')
plt.title('Kết quả học tập của học sinh', fontsize=14)
plt.xlabel('Xếp loại', fontsize=12)
plt.ylabel('Số lượng học sinh', fontsize=12)
plt.show()