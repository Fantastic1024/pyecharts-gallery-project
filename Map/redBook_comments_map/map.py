import pandas as pd
import re
from pyecharts.charts import Map
from pyecharts import options as opts

# 第一步：读取CSV文件
csv_file_path = "xhs_search_comments_2024-05-31.csv"  # 替换为你的CSV文件路径
data = pd.read_csv(csv_file_path, on_bad_lines='skip', encoding_errors="ignore")

# # 第二步：清洗数据

# # 进一步清洗：去除空白字符串或只有空格的字段
data = data[data['ip_location'].str.strip() != '']

# 第三步：处理地理位置数据
# 假设地理位置数据为城市名
# 统计每个城市的出现次数
location_counts = data['ip_location'].value_counts().to_dict()
print(location_counts)
cleaned_data = {}
for key, value in location_counts.items():
    if isinstance(value, int) and not key.isdigit() and not any(char.isdigit() for char in key):
        cleaned_data[key] = value
new_dic = dict(广东=1216, 浙江=478, 四川=436, 江苏=413, 上海=331, 北京=304, 山东=265, 河南=250, 湖南=229, 福建=226,
               湖北=216, 广西=198, 重庆=182, 安徽=164, 陕西=162, 河北=141, 辽宁=133, 江西=131, 云南=111, 天津=88,
               海南=80, 山西=78, 贵州=70, 美国=67, 吉林=63, 黑龙江=58, 新疆=47, 中国=47, 日本=37, 甘肃=37, 内蒙古=33,
               澳大利亚=31, 中国香港=28, 泰国=18, 英国=16, 加拿大=16, 青海=14, 宁夏=12, 德国=11, 马来西亚=10, 新加坡=9,
               西班牙=6, 阿联酋=6, 意大利=5, 中国台湾=5, 韩国=4, 俄罗斯=3, 新西兰=3, 越南=3, 约旦=3, 中国澳门=3, 荷兰=3,
               老挝=3, 南非=2, 瑞士=2, 柬埔寨=2, 法国=2, 西藏=2, 喀麦隆=2, 印度尼西亚=1, 埃及=1,
               尼日利亚=1, 葡萄牙=1, 奥地利=1, 乌干达=1, 爱尔兰=1, 波兰=1, 坦桑尼亚=1, 沙特阿拉伯=1, 白俄罗斯=1, 帕劳=1,
               瑞典=1)

sequence = [(k, v) for k, v in new_dic.items()]
print(sequence)


def map_visualmap(sequence, title) -> Map:
    c = (
        Map(opts.InitOpts(width='1200px', height='600px'))  # 设置画布大小
        .add(series_name="用户数量", data_pair=sequence, maptype="china")  # 添加数据
        .set_global_opts(
            title_opts=opts.TitleOpts(title=title),  # 设置标题
            visualmap_opts=opts.VisualMapOpts(max_=1300, min_=10),  # 设置视觉映射配置
        )
    )
    return c

# 创建地图对象
china_map = map_visualmap(sequence, "中国各省份用户数量")
# 渲染地图到HTML文件
china_map.render(path='china_user_distribution.html')

# # 定义正则表达式来过滤非地理位置的数据
# def is_valid_location(location):
#     if re.match(r'^[\u4e00-\u9fff]+$', location):  # 仅包含中文字符
#         return True
#     if re.match(r'^[A-Za-z\s]+$', location):  # 仅包含英文字符和空格
#         return True
#     return False
#
#
# # 过滤非地理位置的数据
# cleaned_location_counts = {k: v for k, v in location_counts.items() if is_valid_location(k)}
#
# # 标准化地理位置名称的映射字典
# location_mapping = {
#     '美国': 'United States', '英国': 'United Kingdom', '中国香港': 'Hong Kong', '中国台湾': 'Taiwan',
#     '中国澳门': 'Macau', '日本': 'Japan', '澳大利亚': 'Australia', '德国': 'Germany', '马来西亚': 'Malaysia',
#     '新加坡': 'Singapore', '西班牙': 'Spain', '阿联酋': 'United Arab Emirates', '意大利': 'Italy',
#     '韩国': 'South Korea', '俄罗斯': 'Russia', '新西兰': 'New Zealand', '越南': 'Vietnam',
#     '约旦': 'Jordan', '荷兰': 'Netherlands', '老挝': 'Laos', '南非': 'South Africa', '瑞士': 'Switzerland',
#     '柬埔寨': 'Cambodia', '法国': 'France', '喀麦隆': 'Cameroon', '印度尼西亚': 'Indonesia', '埃及': 'Egypt',
#     '尼日利亚': 'Nigeria', '葡萄牙': 'Portugal', '奥地利': 'Austria', '乌干达': 'Uganda', '爱尔兰': 'Ireland',
#     '波兰': 'Poland', '坦桑尼亚': 'Tanzania', '沙特阿拉伯': 'Saudi Arabia', '白俄罗斯': 'Belarus',
#     '帕劳': 'Palau', '瑞典': 'Sweden'
# }
#
# # 应用映射字典标准化地理位置名称
# standardized_location_counts = {location_mapping.get(k, k): v for k, v in cleaned_location_counts.items()}
# print(standardized_location_counts)

# # 创建地图图表
# map_chart = Map()
# map_chart.add("User Locations", [list(z) for z in standardized_location_counts.items()], "china")
# map_chart.set_global_opts(
#     title_opts=opts.TitleOpts(title="User Geographical Distribution"),
#     visualmap_opts=opts.VisualMapOpts(max_=max(standardized_location_counts.values()))
# )
#
# # 渲染图表到HTML文件
# map_chart.render("user_geographical_distribution.html")
