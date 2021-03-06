# -*- coding: utf-8 -*-
"""HuberRegressor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zlzhn3KKaqdyNo9MeGaLYwEKghN_Q8oy
"""

import numpy as np
from sklearn.linear_model import HuberRegressor, LinearRegression
from sklearn.datasets import make_regression

import pandas as pd 
data = pd.read_csv("data.csv",header=None)

X = data[[0,1]].to_numpy()
y = data[[2]].to_numpy().ravel()

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

print(mean_squared_error(LinearRegression().fit(X, y).predict(X),y, squared=False))

mdl = LinearRegression().fit(X, y)

mdl.coef_

mdl.intercept_