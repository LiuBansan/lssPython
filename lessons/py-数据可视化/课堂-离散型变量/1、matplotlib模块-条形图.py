import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']

xdata = ["北京","上海","广州","深圳","南京","重庆","长沙"]
ydata = [2300,1900,1500,1300,1100,2500,800]

plt.bar(xdata, ydata, alpha=0.5, width=0.3, color='yellow', edgecolor='red', label='人口数', lw=3)
plt.legend(loc='upper left')

plt.xlabel('This Is X Axis', fontsize=15)
plt.ylabel('万人', fontsize=15)
plt.title('各个城市人口柱状图', fontsize=15)

# 如果想自己给x轴的bar加上标签,rotation控制倾斜角度
plt.xticks(rotation=30)
plt.yticks(np.arange(0, 2500, 300))

plt.show()
