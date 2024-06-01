from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode

# 示例数据，包含省份名称、经纬度和数值
example_data = [
    ("黑龙江", [127.9688, 45.368, 100]),
    ("内蒙古", [110.3467, 41.4899, 300]),
    ("吉林", [125.8154, 44.2584, 300]),
    ("辽宁", [123.1238, 42.1216, 300]),
    ("河北", [114.4995, 38.1006, 300]),
    ("天津", [117.4219, 39.4189, 300]),
    ("山西", [112.3352, 37.9413, 300]),
    ("陕西", [109.1162, 34.2004, 300]),
    ("甘肃", [103.5901, 36.3043, 300]),
    ("宁夏", [106.3586, 38.1775, 300]),
    ("青海", [101.4038, 36.8207, 300]),
    ("新疆", [87.9236, 43.5883, 300]),
    ("西藏", [91.11, 29.97, 300]),
    ("四川", [103.9526, 30.7617, 300]),
    ("重庆", [108.384366, 30.439702, 300]),
    ("山东", [117.1582, 36.8701, 300]),
    ("河南", [113.4668, 34.6234, 300]),
    ("江苏", [118.8062, 31.9208, 300]),
    ("安徽", [117.29, 32.0581, 300]),
    ("湖北", [114.3896, 30.6628, 300]),
    ("浙江", [119.5313, 29.8773, 300]),
    ("福建", [119.4543, 25.9222, 300]),
    ("江西", [116.0046, 28.6633, 300]),
    ("湖南", [113.0823, 28.2568, 300]),
    ("贵州", [106.6992, 26.7682, 300]),
    ("广西", [108.479, 23.1152, 300]),
    ("海南", [110.3893, 19.8516, 300]),
    ("上海", [121.4648, 31.2891, 1300]),
]

# 创建 Map3D 对象
c = (
    Map3D()
    .add_schema(
        # 设置地图样式
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(5,101,123)",  # 地图颜色
            opacity=1,  # 透明度
            border_width=0.8,  # 边界宽度
            border_color="rgb(62,215,213)",  # 边界颜色
        ),
        # 设置地图标签样式
        map3d_label=opts.Map3DLabelOpts(
            is_show=False,  # 是否显示标签
            formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),  # 标签内容格式
        ),
        # 设置高亮时的标签样式
        emphasis_label_opts=opts.LabelOpts(
            is_show=False,  # 是否显示标签
            color="#fff",  # 标签颜色
            font_size=10,  # 字体大小
            background_color="rgba(0,23,11,0)",  # 背景颜色
        ),
        # 设置光照效果
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",  # 主光源颜色
            main_intensity=1.2,  # 主光源强度
            main_shadow_quality="high",  # 主光源阴影质量
            is_main_shadow=False,  # 是否显示主光源阴影
            main_beta=10,  # 主光源的 β 角度
            ambient_intensity=0.3,  # 环境光强度
        ),
    )
    .add(
        series_name="bar3D",  # 系列名称
        data_pair=example_data,  # 数据
        type_=ChartType.BAR3D,  # 图表类型为 3D 柱状图
        bar_size=1,  # 柱子大小
        shading="lambert",  # 着色方式
        label_opts=opts.LabelOpts(
            is_show=False,  # 是否显示标签
            formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),  # 标签内容格式
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Map3D-Bar3D"))  # 设置全局选项，标题为 "Map3D-Bar3D"
    .render("map3d_with_bar3d.html")  # 渲染图表，输出为 HTML 文件
)
