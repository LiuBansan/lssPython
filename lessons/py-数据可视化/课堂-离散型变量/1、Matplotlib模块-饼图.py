'''
import matplotlib.pyplot as plt

#
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]

data = [255,455,638,565,784,948]
labels = ['博士','硕士','本科','大专','高中','其它']

plt.pie(x = data,               # 数据
         labels = labels,       #标签
         autopct = "%.2a%%")    #格式

plt.show()


'''
import matplotlib.pyplot as plt
# 处理中文乱码
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 标准化处理，确保饼图是个正圆，否则是椭圆
plt.axes(aspect='equal')

#构造数据
data = [255,455,638,565,784,948]
labels = ['博士','硕士','本科','大专','高中','其它']
# 设置突出显示的部分
explode = [0,0.1,0,0,0.15,0]

#绘制饼图
plt.pie(x = data,                # 数据
        labels = labels,         # 标签
        autopct = '%.2f%%',      # 格式
        explode = explode ,      # 突出显示某个部分
        pctdistance = 0.8,       # 百分比标签到圆心的距离
        labeldistance = 1.1,     # 标签到圆心的距离
        startangle = 180,        # 饼图初始角度
        radius = 1.2,            # 饼图半径
        shadow= True,            # 阴影效果
        wedgeprops = {'linewidth':1.5, 'edgecolor':'green'}, # 内外边界属性值
        textprops = {'fontsize':10, 'color':'black'}        # 设置文本标签属性值
        )
plt.title('活动人员学历构成')
plt.show()
