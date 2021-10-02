# pyecharts 数据可视化

import pyecharts
from pyecharts.charts import Bar #柱状图
from pyecharts.charts import Pie #饼图
from pyecharts.charts import Line #折线图
from pyecharts import options as opts  #设置参数


line=Line()

x=["1月","2月","3月","4月","5月","6月"]
y1=[100,200,300,200,100,400]
y2=[50,100,200,300,400,100]

line.add_xaxis(xaxis_data=x)
line.add_yaxis(y_axis=y1,series_name="深圳")
line.add_yaxis(y_axis=y2,series_name="长沙")
line.set_global_opts(title_opts=opts.TitleOpts(title="降雨量折线图"))
line.render("降雨量折线图.html")
