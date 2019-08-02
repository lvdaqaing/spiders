#coding:utf-8

import numpy as np
import pandas as pd
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

myfont = FontProperties(fname='/Users/seancheney/.matplotlib/mpl-data/fonts/ttf/SimHei.ttf')

labels = '朝阳', '海淀', '昌平', '东城', '大兴', '西城', '丰台', '石景山', '通州', '顺义'

df_zf = pd.read_json("ershoufang.json")
chaoyang_count = df_zf['district'].value_counts()['朝阳']
haidian_count = df_zf['district'].value_counts()['海淀']
changping_count = df_zf['district'].value_counts()['昌平']
dongcheng_count = df_zf['district'].value_counts()['东城']
daxing_count = df_zf['district'].value_counts()['大兴']
xicheng_count = df_zf['district'].value_counts()['西城']
fengtai_count = df_zf['district'].value_counts()['丰台']
shijingshan_count = df_zf['district'].value_counts()['石景山']
tongzhou_count = df_zf['district'].value_counts()['通州']
shunyi_count = df_zf['district'].value_counts()['顺义']

sizes = [chaoyang_count, haidian_count, changping_count, dongcheng_count, daxing_count, xicheng_count, fengtai_count, shijingshan_count, tongzhou_count, shunyi_count]
explode = (0.1, 0, 0, 0,0,0,0,0,0,0)
plt.subplot(121)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=-90)
plt.axis('equal')
plt.title("房屋出售分布", fontproperties=myfont)


labels = '朝阳', '海淀', '昌平', '东城', '大兴', '西城', '丰台', '石景山', '通州', '顺义'
df_zf = pd.read_json("zufang.json")
chaoyang_count = df_zf['district'].value_counts()['朝阳']
haidian_count = df_zf['district'].value_counts()['海淀']
changping_count = df_zf['district'].value_counts()['昌平']
dongcheng_count = df_zf['district'].value_counts()['东城']
daxing_count = df_zf['district'].value_counts()['大兴']
xicheng_count = df_zf['district'].value_counts()['西城']
fengtai_count = df_zf['district'].value_counts()['丰台']
shijingshan_count = df_zf['district'].value_counts()['石景山']
tongzhou_count = df_zf['district'].value_counts()['通州']

labels = '朝阳', '海淀', '昌平', '东城', '大兴', '西城', '丰台', '石景山', '通州'
sizes = [chaoyang_count, haidian_count, changping_count, dongcheng_count, daxing_count, xicheng_count, fengtai_count, shijingshan_count, tongzhou_count]
explode = (0.1, 0, 0, 0,0,0,0,0,0)
plt.subplot(122)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=-90)
plt.axis('equal')
plt.title("房屋出租分布", fontproperties=myfont)

plt.rc('font',family=['SimHei'])
plt.show()