import matplotlib.pyplot as plt

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, color='r', lw='2.0', ls='--', label='label')
plt.legend()    # label需要

plt.title("Chart Title", fontsize=20)
plt.xlabel("X-Label", fontsize=14)
plt.ylabel("Y-Label", fontsize=14)

# 座標範圍
plt.xlim(0,20)
plt.ylim(0,100) 

# 格線
plt.grid(color='black', linestyle=':', linewidth='1', alpha=0.5)

plt.show()