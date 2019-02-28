import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']

xdata = ["北京","上海","广州","深圳","南京","重庆","长沙"]
ydata = [2300,1900,1500,1300,1100,2500,800]

sns.barplot(y = ydata,
            x = xdata,
            color = 'steelblue'
            )

plt.xlabel('YLabel')
plt.ylabel('万人')
plt.title('各城市人口柱状图')

plt.show()
