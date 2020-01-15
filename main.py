# coding=utf-8
'''
模型代码：
    参考：https://www.jianshu.com/p/97df66c3a3f8
'''
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor

import config

# 训练样本处理
pdf = pd.read_excel(config.excel_file)
X = list()
# 最低价
Y1 = list()
# 均价
Y2 = list()

for index, element in pdf.iteritems():
    # 去除第一列（字段标识）
    if 'Unnamed' in str(index):
        continue

    # # 去除最后一个（2019年11月），用来验证预测
    # if index==57:
    #     continue

    # # 去除导数第二个（2019年10月），用来验证预测
    # if index == 56:
    #     continue

    # # 去除导数第三个（2019年9月），用来验证预测
    # if index == 55:
    #     continue

    # # 去除导数第四个（2019年8月），用来验证预测
    # if index == 54:
    #     continue

    l_element = element.tolist()
    # 全部特征
    # X.append(l_element[0:6])
    # 只使用前两次竞价价格
    X.append(l_element[4:6])
    Y1.append(l_element[6])
    Y2.append(l_element[7])

# print(X)
# print(Y1)
# print(Y2)

# 多模型初始化
l_models = list()
model = linear_model.LinearRegression()
l_models.append(model)
model = SVR(kernel='linear')
l_models.append(model)
# 运行速度非常慢（半天跑不完）
# model=SVR(kernel="poly")
model = SVR(kernel="rbf")
l_models.append(model)
model = KNeighborsRegressor(weights="uniform")
l_models.append(model)
# 树模型中，random_state参数会导致结果波动
model = DecisionTreeRegressor()
l_models.append(model)
model = RandomForestRegressor()
l_models.append(model)
model = ExtraTreesRegressor()
l_models.append(model)
model = GradientBoostingRegressor()
l_models.append(model)

# 测试单个模型
# model = linear_model.LinearRegression()
# model=SVR(kernel='linear')
# model=SVR(kernel="rbf")
# model=KNeighborsRegressor(weights="uniform")
# 树模型中，random_state参数会导致结果波动
# model=DecisionTreeRegressor()
# model=RandomForestRegressor()
# model=ExtraTreesRegressor()
model = GradientBoostingRegressor()

# 待预测特征（实际预测时，只要初始化特征x即可）
# # 2019.08
# x = [[23151, 25107]]
# # 2019.09
# x = [[26412, 28139]]
# # 2019.10特征
# x = [[28871, 30719]]
# # 2019.11特征
# x=[[29060, 31156]]
# # 2019.12
x = [[24563, 26085]]
# 待预测最低价
model.fit(X, Y1)
y1 = model.predict(x)
# 待预测平均价
model.fit(X, Y2)
y2 = model.predict(x)
print('---------单个模型-----------')
print('预测最低价格：{}'.format(y1))
print('预测均值价格:{}'.format(y2))

# 测试所有模型bagging
l_y1 = list()
l_y2 = list()

for m in l_models:
    m.fit(X, Y1)
    y1 = m.predict(x)
    l_y1.append(y1)

    m.fit(X, Y2)
    y2 = m.predict(x)
    l_y2.append(y2)

y1 = np.mean(l_y1)
y2 = np.mean(l_y2)
print('---------多模型bagging-----------')
print('预测最低价格：{}'.format(y1))
print('预测均值价格:{}'.format(y2))
