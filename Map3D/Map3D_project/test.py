from pyecharts import options as opts
from pyecharts.charts import Map3D
import pandas as pd
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode

# 第一步：读取CSV文件
csv_file_path = "xhs_search_comments_2024-05-31.csv"  # 替换为你的CSV文件路径
data = pd.read_csv(csv_file_path, on_bad_lines='skip', encoding_errors="ignore")

# # 第二步：清洗数据

# # 进一步清洗：去除空白字符串或只有空格的字段
data = data[data['ip_location'].str.strip() != '']

# 第三步：处理地理位置数据
# 假设地理位置数据为城市名
# 统计每个城市的出现次数 (统计了不同省份的评论数据)
# 数据，包含省份名称和数值
location_counts = data['ip_location'].value_counts().to_dict()  #将相同省份出现的评论数相加得到
# print(location_counts)
cleaned_data = {}
for key, value in location_counts.items():
    if isinstance(value, int) and not key.isdigit() and not any(char.isdigit() for char in key):
        cleaned_data[key] = value

# 中国省份列表
china_provinces = [
    '北京', '天津', '上海', '重庆', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽',
    '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南', '四川', '贵州', '云南', '陕西',
    '甘肃', '青海', '台湾', '内蒙古', '广西', '西藏', '宁夏', '新疆'
]

# 示例数据，包含省份名称、经纬度和数值(后期增加了例子中所没有的部分)
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
    ("北京", [116.4551, 40.2539, 1300]),
    ("广东", [113.5107, 23.2196, 1300]),
    ("香港", [114.1655, 22.2753, 1300]),
    ("澳门", [113.5491, 22.1987, 1300]),
    ("台湾", [121.509062, 25.044332, 1300])
]
# 过滤数据，只保留中国省份
filtered_data = {province: count for province, count in cleaned_data.items() if province in china_provinces}
sequence = [(k, v) for k, v in filtered_data.items()]
# 输出清洗后的数据
print(sequence)

# 更新 example_data 中的评论计数
updated_example_data = [
    (province, [coords[0], coords[1], filtered_data.get(province, 0)]) for province, coords in example_data
]

# 打印更新后的数据
print(updated_example_data)

# 创建 Map3D 对象
c = (
    Map3D()
    .add_schema(
        itemstyle_opts=opts.ItemStyleOpts(
            color="rgb(0, 128, 255)",  # 更鲜艳的蓝色
            opacity=0.8,  # 透明度
            border_width=1,  # 边界宽度
            border_color="rgb(255, 255, 255)",  # 边界颜色为白色
        ),
        map3d_label=opts.Map3DLabelOpts(
            is_show=False,
            formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
        ),
        emphasis_label_opts=opts.LabelOpts(
            is_show=False,
            color="#fff",
            font_size=10,
            background_color="rgba(0,23,11,0)",
        ),
        light_opts=opts.Map3DLightOpts(
            main_color="#fff",
            main_intensity=1.5,  # 增加主光源强度
            main_shadow_quality="high",
            is_main_shadow=False,
            main_beta=30,  # 调整主光源的 β 角度
            ambient_intensity=0.5,  # 增加环境光强度
        ),
    )
    .add(
        series_name="评论数量",
        data_pair=updated_example_data,
        type_=ChartType.BAR3D,
        bar_size=1.5,  # 增加柱子大小
        shading="lambert",
        label_opts=opts.LabelOpts(
            is_show=True,
            color="#000",  # 标签文字颜色为黑色
            font_size=12,  # 增大字体大小
            formatter=JsCode("function(data){return data.name + ' ' + data.value[2];}"),
        ),
        # itemstyle_opts=opts.ItemStyleOpts(
        #     color=JsCode(
        #         """
        #         new echarts.graphic.LinearGradient(0, 0, 0, 1, [
        #             { offset: 0, color: 'rgb(255, 0, 0)' },  # 红色
        #             { offset: 1, color: 'rgb(255, 255, 0)' }  # 黄色
        #         ])
        #         """
        #     ),
        # ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="3D不同省份关于“旅游”话题的讨论次数"))
    .render("map3d_with_bar3d.html")
)