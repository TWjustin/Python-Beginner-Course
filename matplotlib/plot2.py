import matplotlib.pyplot as plt
year = [2015,2016,2017,2018,2019]
city1 = [128,150,199,180,150]
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="台北")
city2 = [120,145,180,170,120]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="台中")
plt.legend()
plt.ylim(50, 250)   # 範圍
plt.xticks(year)    # 自訂座標刻度
plt.title("銷售報表", fontsize=18)
plt.xlabel("年度", fontsize=12)
plt.ylabel("百萬", fontsize=12)
plt.grid(color='k', ls=':', lw=1, alpha=0.5)

# 設定中文字型及正負號正確顯示
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False
plt.show()