#!/usr/bin/python
import akshare as ak
import pandas as pd

fund_num='110010'
data="单位净值走势"

fund_em_info_df = ak.fund_em_open_fund_info(fund=fund_num, indicator=data)

df = fund_em_info_df.astype({'x':'datetime64','y':'float','equityReturn':'float'})
print(df)

df.plot(x='x',y='y').get_figure().savefig('fund.jpg')

