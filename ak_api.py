#!/usr/bin/python
import akshare as ak

stock='sh000001'

#data = ak.stock_zh_index_daily(stock)
data = ak.fund_em_open_fund_rank()
print(data)
