# coding=utf-8
'''
历史数据处理：
    将原始的网页数据整理为excel数据
    网页地址：https://m.baidu.com/ala/c/m.bendibao.com/mip/775782.html
'''

import pandas as pd
import config

# 年
year = list()
# 期
month = list()
# 指标数
valid_num = list()
# 编码数
join_num = list()
# 第一次报价均值
first_price = list()
# 第二次报价均值
second_price = list()
# 最低成交价
lowest_price = list()
# 平均成交价
average_price = list()

f = open(config.web_data_file, 'r')
for line in f.readlines():
    line_data = line.split()
    if len(line_data) == 7:
        c_year = line_data[0]
        c_year = c_year.replace('年', '')
        year.append(c_year)

        valid_num.append(line_data[1])
        join_num.append(line_data[2])
        first_price.append(line_data[3])
        second_price.append(line_data[4])
        lowest_price.append(line_data[5])
        average_price.append(line_data[6])

    if len(line_data) == 1:
        c_month = line_data[0]
        c_month = c_month.replace('第', '')
        c_month = c_month.replace('期', '')
        month.append(c_month)

f.close()

pdf = pd.DataFrame([year, month, valid_num, join_num, first_price, second_price, lowest_price, average_price],
                   index=['year', 'month', 'valid_num', 'join_num', 'first_price', 'second_price', 'lowest_price',
                          'average_price'])
pdf.to_excel(config.excel_file)

print('preprocess is Done!')
