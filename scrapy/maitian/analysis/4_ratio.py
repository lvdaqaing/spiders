# 售租比

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

district = ('西城', '石景山','东城','海淀','丰台','昌平','大兴','朝阳', '通州')

# 读取租房数据
df_zf = pd.read_json("zufang.json")
unitprice_zf = df_zf['price']/df_zf['area']
df_zf['unitprice'] = unitprice_zf

# print(df_zf)

month_price = df_zf.groupby(by=['district']).sum()['unitprice'] / df_zf["district"].value_counts()

# print(month_price)

# # 读取二手房数据
df_esf = pd.read_json("ershoufang.json")

sell_price = df_esf.groupby(by=['district']).sum()['unitprice']/df_esf["district"].value_counts()

# print(sell_price)

xicheng_ratio = sell_price['西城'] / month_price['西城']
shijingshan_ratio = sell_price['石景山'] / month_price['石景山']
dongcheng_ratio = sell_price['东城'] / month_price['东城']
haidian_ratio = sell_price['海淀'] / month_price['海淀']
fengtai_ratio = sell_price['丰台'] / month_price['丰台']
changping_ratio = sell_price['昌平'] / month_price['昌平']
daxing_ratio = sell_price['大兴'] / month_price['大兴']
chaoyang_ratio = sell_price['朝阳'] / month_price['朝阳']
tongzhou_ratio = sell_price['通州'] / month_price['通州']
#
#
ratio = (
    xicheng_ratio,
    shijingshan_ratio,
    dongcheng_ratio,
    haidian_ratio,
    fengtai_ratio,
    changping_ratio,
    daxing_ratio,
    chaoyang_ratio,
    tongzhou_ratio
)

fig, ax = plt.subplots()

y_pos = np.arange(len(district))
# performance = ratio

ax.barh(y_pos, ratio, align='center', color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(district)
# ax.invert_yaxis()
ax.set_xlabel('售租比（单位:月）')
ax.set_title('各区房屋售租比')

plt.show()