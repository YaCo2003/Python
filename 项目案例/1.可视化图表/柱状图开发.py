# #1.基础柱状图
#
# from pyecharts.charts import Bar
# from pyecharts.options import *
# bar=Bar()
#
# bar.add_xaxis(["中国","美国","英国"])
# bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(
#     position="right"
# ))
#
# # 反转x和y
# bar.reversal_axis()
# bar.render()

# # 2.基础时间线
# from pyecharts.charts import Bar, Timeline
# from pyecharts.options import *
# from pyecharts.globals import *
#
# bar1 = Bar()
# bar1.add_xaxis(["中国", "美国", "英国"])
# bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(
#     position="right"
# ))
# bar1.reversal_axis()
# bar1.render()
#
# bar2 = Bar()
# bar2.add_xaxis(["中国", "美国", "英国"])
# bar2.add_yaxis("GDP", [50, 40, 30], label_opts=LabelOpts(
#     position="right"
# ))
# bar2.reversal_axis()
# bar2.render()
#
# bar3 = Bar()
# bar3.add_xaxis(["中国", "美国", "英国"])
# bar3.add_yaxis("GDP", [70, 50, 60], label_opts=LabelOpts(
#     position="right"
# ))
# bar3.reversal_axis()
# bar3.render()
#
# # 构建时间线对象
# timeline = Timeline(
#     {"theme":ThemeType.INFOGRAPHIC}
# )
# # 添加对象
# timeline.add(bar1, "点1")
# timeline.add(bar2, "点2")
# timeline.add(bar3, "点3")
# # 绘图使用时间线绘图
# timeline.render("基础时间线绘图.html")
# # 设置自动播放
# timeline.add_schema(
#     play_interval=500,  # 自动播放时间间隔，1000ms
#     is_timeline_show=True,  # 是否播放时显示时间线
#     is_auto_play=True,  # 是否自动播放
#     is_loop_play=True  # 是否循环自动播放
# )

# GDP动态图表绘制
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import *

# 数据处理：1.从文件中读取数据 2.将json转换为列表

f = open("./动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GBK")
data_lines = f.readlines()
f.close()
data_lines.pop(0)
# 转成字典
data_dict = {}
for line in data_lines:
    year = (int(line.split(",")[0]))  # 年份
    country = line.split(",")[1]  # 国家
    gdp = float(line.split(",")[2])  # gdp
    # 如何判断字典里有没有指定的数数据key呢？
    # 捕获异常，不存在先添加年份，再追加，存在就直接追加
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# 时间线对象
timeline = Timeline({"theme": ThemeType.INFOGRAPHIC})
# 排序年份
# 1。先取所有年份
sorted_year_list = sorted(data_dict.keys())
# 2.对每一年的gdp排序，取前8,单次for是构建单独一年的表
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出前八名
    year_data = data_dict[year][0:8]
    # 构建x，y轴
    x_data = []
    y_data = []
    for element in year_data:
        x_data.append(element[0])  # x轴国家
        y_data.append(element[1] / 100000000)  # y轴gdp 以亿为单位
    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(
        position="right"
    ))
    # 反转x和y
    bar.reversal_axis()
    #设置图表标题
    bar.set_global_opts(
        title_opts=TitleOpts(
            title=f"{year}年全球前八GDP数据"
        )
    )
    #添加时间线
    timeline.add(bar,str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=1000,  # 自动播放时间间隔，1000ms
    is_timeline_show=True,  # 是否播放时显示时间线
    is_auto_play=True,  # 是否自动播放
    is_loop_play=True  # 是否循环自动播放
)
# 绘图使用时间线绘图
timeline.render("1960-2019全球GDP前八国家.html")