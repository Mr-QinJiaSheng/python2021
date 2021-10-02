# pyecharts 数据可视化

# *******
# pyecharts 是一个用于生成 Echarts 图表的类库。
# Echarts 是百度开源的一个数据可视化 JS 库。
# 用 Echarts 生成的图可视化效果非常棒.

# ***下载：
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts

# ***新版v1和老版本不兼容，如果需要使用老版本，下载：
# pip install pyecharts==0.5.5

import pyecharts
from pyecharts.charts import Bar #柱状图
from pyecharts.charts import Pie #饼图
from pyecharts.charts import Line #折线图
from pyecharts import options as opts  #设置参数

bar=Bar() #创建柱状图对象
bar.add_xaxis(["衬衫","毛衣","裙子","风衣","T恤"]) #添加x轴数据
bar.add_yaxis("A商家销量",[150,67,95,78,99]) #添加y轴数据
bar.add_yaxis("B商家销量",[170,167,145,28,19]) #添加y轴数据
bar.add_yaxis("C商家销量",[120,67,125,58,89]) #添加y轴数据
bar.set_global_opts(title_opts=opts.TitleOpts(title="商场销售情况")) #设置标题
bar.render("商场销售柱状图.html")
