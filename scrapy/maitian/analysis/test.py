import pandas as pd

df_zf = pd.read_json("zufang.json")

# df_zf_pd = pd.DataFrame(df_zf)

# print(df_zf_pd.head())

unitprice_zf = df_zf['price']/df_zf['area']
# print(unit_price)

df_zf['unitprice'] = unitprice_zf

print(df_zf.describe())
#
print(df_zf['district'].value_counts())
#
#
# print(df_zf['district'] == '朝阳')

month_price = df_zf.groupby(by=['district']).sum()['unitprice']/df_zf["district"].value_counts()

df_esf = pd.read_json("ershoufang.json")

sell_price = df_esf.groupby(by=['district']).sum()['unitprice']/df_esf["district"].value_counts()

# print((df_zf.groupby(by=['district']).sum()['unitprice']/df_zf["district"].value_counts())['朝阳'])
#
#
# df_esf = pd.read_json("ershoufang.json")
# print((df_esf.groupby(by=['district']).sum()['unitprice']/df_esf["district"].value_counts())['朝阳'])

# ratio = (df_esf.groupby(by=['district']).sum()['unitprice']/df_esf["district"].value_counts())['朝阳'] / (df_zf.groupby(by=['district']).sum()['unitprice']/df_zf["district"].value_counts())['朝阳']

district = '朝阳'
ratio = sell_price[district] / month_price[district]

print(ratio)