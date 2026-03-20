import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
y1 = x**2
ax1.plot(x, y1, color='blue', linewidth=2)
ax1.set_title('Đồ thị $y = x^2$', fontsize=14)
ax1.set_xlabel('Trục X', fontsize=12)
ax1.set_ylabel('Trục Y', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
y2 = np.sqrt(x)
ax2.plot(x, y2, color='green', linewidth=2)
ax2.set_title('Đồ thị $y = \\sqrt{x}$', fontsize=14)
ax2.set_xlabel('Trục X', fontsize=12)
ax2.set_ylabel('Trục Y', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()