# encoding: utf-8

import pandas as pd

# 租房 基本信息

# 读取文件 df=dataframe
df = pd.read_json("zufang.json")
# print(df)
# print(df.columns)

# 使用pandas的describe方法，打印基本信息
print(df.describe())
# 按照区，分别统计个数
print(
    df["district"].value_counts()
)
#
# print('**************************')
#
# # 二手房 基本信息
df = pd.read_json("ershoufang.json")
print(df.describe())
#分别统计个数
print(df["district"].value_counts())