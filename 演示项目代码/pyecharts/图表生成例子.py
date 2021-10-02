'''
下载：
pip install pyecharts
pip install snapshot-selenium

pyecharts 是一个用于生成 Echarts 图表的类库。
Echarts 是百度开源的一个数据可视化 JS 库。
用 Echarts 生成的图可视化效果非常棒

新版v1和老版本不兼容，如果需要使用老版本，下载：
pip install pyecharts==0.5.5

'''

import pyecharts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Line
from pyecharts import options as opts  #设置参数

# #基本柱状图
# bar = Bar()
# bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
# bar.add_yaxis("销量", [114, 55, 27, 101, 125, 27, 105])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="商场销售情况"))
# bar.render("柱状图1.html")

#并列柱状图
# bar = Bar()
# bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
# bar.add_yaxis("商家B", [14, 5, 7, 11, 25, 27, 10])
# bar.add_yaxis("商家C", [57, 134, 137, 129, 145, 60, 49])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# bar.render("柱状图2.html")


# #饼状图
pie=Pie()
cate = ['苹果', '华为', '小米', 'Oppo', 'Vivo', '魅族']
data = [153, 124, 107, 99, 89, 46]
#[['苹果', 153], ['华为', 124], ['小米', 107], ['Oppo', 99], ['Vivo', 89], ['魅族', 46]]
dataList=[]
for i in range(0,len(cate)):
	d=[cate[i],data[i]]
	dataList.append(d)
pie.set_global_opts(title_opts=opts.TitleOpts(title="手机品牌销售情况"))
pie.add('单位（万台）',dataList)
pie.render("饼图1.html")


# # #饼状图-圈图
# pie=Pie()
# cate = ['苹果', '华为', '小米', 'Oppo', 'Vivo', '魅族']
# data = [153, 124, 107, 99, 89, 46]
# dataList=[]
# for i in range(0,len(cate)):
# 	d=[cate[i],data[i]]
# 	dataList.append(d)
# pie.add('单位（万台）', dataList,radius=["50%", "70%"],rosetype="radius")
# pie.set_global_opts(title_opts=opts.TitleOpts(title="手机品牌销售情况"))
# pie.render("饼图2.html")


#折线图
x=['1月','2月','3月','4月','5月','6月','7月']
y1=[100,200,300,400,100,400,300]
y2=[200,300,200,100,200,300,400]
line=Line()
line.add_xaxis(xaxis_data=x)
line.add_yaxis(series_name="深圳",y_axis=y1)
line.add_yaxis(series_name="长沙",y_axis=y2)
line.set_global_opts(title_opts=opts.TitleOpts(title="降水量变化（ml）"))
line.render("折线图1.html")


#也直接生成图片，但需要设置的内容较多，需要的时候直接生成网页然后截取图片即可



