import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt


from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_json("ershoufang.json")

print(df.columns)

unitprice_values = df.unitprice
plt.hist(unitprice_values,
         bins=25
         )
plt.xlim(0,200000)
plt.title(u"房屋出售每平米价格分布")
plt.xlabel(u'价格(单位:万/平方米)')
plt.ylabel(u'套数')
plt.show()