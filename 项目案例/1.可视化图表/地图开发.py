# from pyecharts.charts import Map
# from pyecharts.options import *

# # 基础地图演示
# map = Map()
# data = [
#     ("北京市", 99),
#     ("上海市", 199),
#     ("湖南省", 299),
#     ("台湾省", 399),
#     ("广东省", 499)
# ]
# # 添加数据
# map.add("测试地图", data, "china")
#
# # 设置全局选项
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min": 1, "max": 9, "label": "1-9人", "color": "#CCFFFF"},
#             {"min": 10, "max": 99, "label": "10-99人", "color": "#FFFF99"},
#             {"min": 100, "max": 999, "label": "100-999人", "color": "#FF9966"}
#
#         ]
#     )
# )
# # 绘图
# map.render()

# # 疫情地图
# from pyecharts.charts import Map
# from pyecharts.options import *
# import json
#
# # 读取数据
# f = open("./地图数据/疫情.txt", "r", encoding="UTF-8")
# data = f.read()
# f.close()
#
# # 将json-》python字典
# data_dict = json.loads(data)
#
# # 取出字典中省份数据
# province_data_list = data_dict["areaTree"][0]["children"]
#
# # 取出每个省份的名称和确诊人数，并将其封装入列表中
# data_list = []
# for province_data in province_data_list:
#     province_name = province_data["name"] + "省"
#     province_confirm = province_data["total"]["confirm"]
#     data_list.append((province_name, province_confirm))
#
# map = Map()
# print(data_list)
# map.add("各个省份确诊人数", data_list, "china")
# # 设置全局选项
# map.set_global_opts(
#     title_opts=TitleOpts(title="全国疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,  # 是否显示
#         is_piecewise=True,  # 是否分段
#         pieces=[
#             {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
#             {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
#             {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
#             {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
#             {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
#             {"min": 100000, "label": "100000人以上", "color": "#990033"}
#         ]
#     )
# )
# # 绘图
# map.render("全国疫情地图.html")

# 河南省疫情地图
from pyecharts.charts import Map
from pyecharts.options import *
import json

# 读取数据
f = open("./地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()

# 将json-》python字典
data_dict = json.loads(data)

# 取出字典中省份数据
city_data_list = data_dict["areaTree"][0]["children"][3]["children"]

# 取出每个省份的名称和确诊人数，并将其封装入列表中
data_list = []
for city__data in city_data_list:
    city__name = city__data["name"] + "市"
    city__confirm = city__data["total"]["confirm"]
    data_list.append((city__name, city__confirm))
# 手动添加
data_list.append(("济源市", 5))
map = Map()
print(data_list)
map.add("河南省疫情分布", data_list, "河南")
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},

        ]
    )
)
# 绘图
map.render("河南省疫情地图.html")
