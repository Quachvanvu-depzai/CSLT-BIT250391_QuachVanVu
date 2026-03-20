import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("C:\\california_cities.csv")
df = pd.DataFrame(data)
top10_cities = df.sort_values(by='area_total_km2', ascending=False).head(10)
top10_cities = top10_cities.sort_values(by='area_total_km2', ascending=True)
plt.barh(top10_cities['city'], top10_cities['area_total_km2'], color='mediumseagreen')
plt.title('Top 10 thành phố lớn nhất theo diện tích ở California', fontsize=14)
plt.xlabel('Diện tích (km²)', fontsize=12)
plt.ylabel('Thành phố', fontsize=12)
plt.tight_layout()
plt.show()