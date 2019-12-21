# coding=utf-8
'''
模型代码：
    参考：https://blog.csdn.net/hubingshabi/article/details/80172608
    参考：https://www.jianshu.com/p/97df66c3a3f8
'''
import pandas as pd
from sklearn import linear_model
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor

import config

pdf = pd.read_excel(config.excel_file)

# print(type(pdf[0]))

X = list()
# 最低价
Y1 = list()
# 均价
Y2 = list()

# print(type(pdf))

for index, element in pdf.iteritems():
    # 去除第一列（字段标识）
    if 'Unnamed' in str(index):
        continue

    l_element = element.tolist()
    X.append(l_element[0:6])
    Y1.append(l_element[6])
    Y2.append(l_element[7])

print(X)
print(Y1)
print(Y2)

# 拟合误差非常大
# model = linear_model.LinearRegression()
# model=SVR(kernel='linear')
# 运行速度非常慢（半天跑不完）
# model=SVR(kernel="poly")
# 误差很大
# model=SVR(kernel="rbf")
# model=KNeighborsRegressor(weights="uniform")
# 完全拟合
# model=DecisionTreeRegressor()
# model=RandomForestRegressor()
# 完全拟合
# model=ExtraTreesRegressor()
# 比较接近
model = GradientBoostingRegressor()

model.fit(X, Y1)

predic_x = [[2015, 1, 3912, 1578, 15522, 17021], [2015, 2, 6491, 742, 12385, 12637],
            [2015, 3, 9878, 10281, 11225, 11341], [2015, 4, 3880, 10646, 11198, 11426]]
predic_y = model.predict(predic_x)
print(predic_y)
