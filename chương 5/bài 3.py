import matplotlib.pyplot as plt
san_pham = ['Sản phẩm A', 'Sản phẩm B', 'Sản phẩm C', 'Sản phẩm D', 'Sản phẩm E']
phan_tram = [30, 25, 15, 20, 10]
mau_sac = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
plt.pie(phan_tram, labels=san_pham, colors=mau_sac, autopct='%1.1f%%', startangle=140)
plt.title('Phần trăm doanh số của 5 sản phẩm', fontsize=14)
plt.show()