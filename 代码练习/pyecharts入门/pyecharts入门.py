from pyecharts.charts import Line
from pyecharts.options import ToolboxOpts

line = Line()
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])

# 全局配置项
line.set_global_opts(
    toolbox_opts=ToolboxOpts(is_show=True)
)
line.render()
