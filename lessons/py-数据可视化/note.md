# 数据可视化

文不如字，字不如表，表不如图，这句话充分说明了可视化的重要性。从事与数据相关的工作者经常会作一些总结或者展望性的报告，如果报告中密密麻麻的都是文字，相信听众和老板一定会烦，如果报告中呈现的是大量的图形化结果，就会边到众人的喜爱，因为图形更加直观醒目。本章的重点就是利用Python绘制常见的统计图形，如条形图、饼图、直方图、折线图、散点图等。这些图形的绘制可以通过matplotlib模块、pandas模块或者seaborn模块实现。
Matplotlib是最流行的用于制图及其它二维数组可视化的库，它与生态系统的其他库良好整合。
## 离散型变量

### 饼图

饼图，也叫饼状图，是一个划分为几个扇区的圆形统计图表，用于描述量、频率、或百分比之间的相对关系。在饼图中，每个扇区的弧长（圆心角和面积）大小为其所表示的数量的比例。这些扇区合在一起刚好是一个完整的圆形，这些扇区就好像拼成一个切开的饼形图案。

1、Matplotlib模块
- [Matplotlib 教程](http://www.runoob.com/w3cnote/matplotlib-tutorial.html)
首先要导入matplotlib模块的子模块pyplot，然后利用模块中的pie函数。
- 注意：
    - 如果绘制的图中涉及中文及数字中的负号，需要通过rcParams进行了控制；
    - 不加修饰的饼图更像是一个椭圆，所以需要利用axes函数强制为正圆。
    
2、Pandas模块
（1）示例



### 条形图

条形图亦称条图、条状图、棒形图、柱状图，是一种以长方形的长度为变量的统计图表。长条图用来比较两个或者两个以上的数值（不同时间或者不同条件），只有一个变量，通常利用最小的数据集分析。
长条图也可横向排列，也可用多维表达方式。

1、matplotlib模块
matplotlib.pyplot.bar(left, height, alpha=1, width=0.8, color=, edgecolor=, label=, lw=3)
    
    1. left：x轴的位置序列，一般采用range函数产生一个序列，但是有时候可以是字符串
    2. height：y轴的数值序列，也就是柱形图的高度，一般就是我们需要展示的数据；
    3. alpha：透明度，值越小越透明
    4. width：为柱形图的宽度，一般这是为0.8即可；
    5. color或facecolor：柱形图填充的颜色；
    6. edgecolor：图形边缘颜色
    7. label：解释每个图像代表的含义，这个参数是为legend()函数做铺垫的，表示该次bar的标签
    8. linewidth or linewidths or lw：边缘or线的宽

2、Pandas模块
    
    pandas模块都是用 xx.plot 
    
    = 例如：
            data.plot(kind = 'bar',
                  width =0.4,
                  rot = 0,
                  color='steelblue',
                  title = '各城市口柱状图')


