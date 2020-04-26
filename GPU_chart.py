import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib

# 设置字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文

# 设置图片大小
plt.figure(figsize=(16, 9), dpi=80)
# GPU型号
X = ["RTX 2080Ti", "RTX 2080S", "GTX 1080Ti", "RTX 2070S", "RTX 2060S", "RTX 2060", "GTX 1660Ti", "GTX 1650", "RX 580"]
# 产品价格
Ave_Prices = [12999, 6799, 5599, 4499, 3589, 2899, 2359, 1149, 1099]
# 性能综合评分
Ana_Grades = [16698, 15885, 14223, 14862, 13830, 12849, 11519, 7944, 8560]

# 画折线图
plt.plot(range(len(X)), Ave_Prices, marker='*', linewidth=3, label='a', color='r')

# 画条形图
# plt.bar(range(len(X)), Ana_Grades, width=0.6)
plt.bar(range(len(X)), height=Ana_Grades, label='b', color='steelblue', alpha=0.8)
# 坐标标识
plt.xticks(range(len(X)), X, rotation=45)
# 图形说明
plt.title("GPU性能价格对比图", fontsize=25, )
plt.xlabel("GPU型号", fontsize=25,)

# 设置标注
plt.legend(loc="upper right")

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=15)
# 显示图像
plt.show()