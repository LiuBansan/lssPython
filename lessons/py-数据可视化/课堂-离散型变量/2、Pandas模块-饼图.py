import pandas as pd
import matplotlib.pyplot as plt

# 处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

data = pd.Series({'博士':255,'硕士':455,'本科':638,'大专':565,'高中':784,'其它':948,})
data.name = '学历构成'
data.plot(kind = 'pie',
          autopct = '%.2f%%',
          radius = 1,
          startangle = 180,
          title = '活动人员学历构成',
          wedgeprops = {'linewidth':1.5, 'edgecolor':'green'}, # 内外边界属性值
          textprops = {'fontsize':10, 'color':'black'}      # 设置文本标签属性值
          )
#显示图形
plt.show()
