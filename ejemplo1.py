import pandas as pd
import numpy as np

data1 = pd.Series(['TABLET','LAPTOP','PC','CELULAR','MONITOR','DVD'], index=[1,2,3,4,5,6])
print(data1)

data2 = pd.Series({'ENERO':45000, 'FEBRERO':38000, 'MARZO':50000})
print(data2)

data3 = pd.Series(np.random.randn(10))
print(data3)
print(data3.head())
print((data3.tail()))
print(data3.head(2))
print((data3.tail(2)))