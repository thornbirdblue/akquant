#!/usr/bin/python
import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

fund_num='110003'
data="单位净值走势"

name_df = ak.fund_em_fund_name()
fund_name=fund_num+name_df.loc[name_df['基金代码']==fund_num]['基金简称'].item()

fund_em_info_df = ak.fund_em_open_fund_info(fund=fund_num, indicator=data)
df = fund_em_info_df.astype({'x':'datetime64','y':'float','equityReturn':'float'})
print(df)

df.plot(x='x',subplots=True,title=fund_name)

plt.savefig('fund.jpg')
