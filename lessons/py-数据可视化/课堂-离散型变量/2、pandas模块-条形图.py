import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']

data = pd.Series([2300,1900,1500,1300,1100,2500,800],
                 index = ["北京","上海","广州","深圳","南京","重庆","长沙"])
data.plot(kind = 'bar',
          width =0.4,
          rot = 0,
          color='steelblue',
          title = '各城市口柱状图')
plt.show()
