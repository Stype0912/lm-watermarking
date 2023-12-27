import matplotlib.pyplot as plt

# 数据
percentage = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
w_bl_avg_PPL = [2.321664059, 2.445243216, 2.566769636, 2.721479064, 2.536122334, 2.613334721, 2.883200043,
                2.807317245, 2.584756452, 2.663658303]
no_bl_avg_PPL = [2.34818123] * len(percentage)
w_bl_avg_loss = [0.829667169, 0.875507799, 0.916653734, 0.972057199, 0.900492297, 0.930529678, 1.017116866,
                 1.001510558, 0.923012112, 0.949077183]
no_bl_avg_loss = [0.829972672] * len(percentage)

# 绘制散点图
plt.scatter(percentage, w_bl_avg_PPL, label="wm avg PPL", marker="s")
plt.scatter(percentage, no_bl_avg_PPL, label="non_wm avg PPL", marker="p")
plt.scatter(percentage, w_bl_avg_loss, label="wm avg loss", marker="o")
plt.scatter(percentage, no_bl_avg_loss, label="non_wm avg loss", marker="D")

# 设置图表标题和坐标轴标签
# plt.title("Scatter Plot")
plt.xlabel("Percentage")
plt.ylabel("Value")

# 添加图例
plt.legend()

# 显示图表
plt.show()
