# pyecharts 数据可视化

import pyecharts
from pyecharts.charts import Bar #柱状图
from pyecharts.charts import Pie #饼图
from pyecharts.charts import Line #折线图
from pyecharts import options as opts  #设置参数

pie=Pie() #创建饼状图对象
cate = ['苹果', '华为', '小米', 'Oppo', 'Vivo', '魅族']
data = [153, 124, 107, 99, 89, 46]
dataList=[] #数据处理
for i in range(0,len(cate)):
	d=[cate[i],data[i]]
	dataList.append(d)
pie.set_global_opts(title_opts=opts.TitleOpts(title="手机销售情况"))
pie.add("单位：万台",dataList)
pie.render("手机销量饼图.html")
