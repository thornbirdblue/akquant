#!/usr/bin/python
import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

fund_num='110003'
#data="单位净值走势"
data="累计收益率走势"

name_df = ak.fund_em_fund_name()
fund_name=fund_num+name_df.loc[name_df['基金代码']==fund_num]['基金简称'].item()

df = ak.fund_em_open_fund_info(fund=fund_num, indicator=data)
#df['日增长率']=df['日增长率'].astype('float')
print(df)

df.plot(x='净值日期',figsize=(20,10),grid=True,title=fund_name).get_figure().savefig('fund.jpg')
#df.plot(x='净值日期',figsize=(20,10),grid=True,title=fund_name,secondary_y=['日增长率']).get_figure().savefig('fund.jpg')

