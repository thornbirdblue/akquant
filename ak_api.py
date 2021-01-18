#!/usr/bin/python
import akshare as ak

stock='sh000001'

data = ak.stock_zh_index_daily(stock)
print(data)
