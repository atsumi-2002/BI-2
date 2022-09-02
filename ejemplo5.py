import pandas as pd
import numpy as np

data1 = pd.DataFrame(np.array([['Enero','Febrero','Marzo'],
                       [40000,35000,50000],
                       [56000,60000,24000],
                       [88000,77000,55000]]))
print(data1)
print('Filas y columnas: ',data1.shape)
print('Altura: ', len(data1.index))
print('Ancho: ', len(data1.count()))

data2 = pd.DataFrame(np.array([[40000,35000,50000],
                       [56000,60000,24000],
                       [88000,77000,55000]]))
print(data2)
print(data2.describe())
print('Media:')
print(data2.mean())
print('Correlacion:')
print(data2.corr())
print('Mediana:')
print(data2.median())
print('Mas alto:')
print(data2.max())
print('Mas bajo:')
print(data2.min())
print('Des. estandar:')
print(data2.std())
print('Primera y segunda columna:')
print(data2[[0,1]])
print('Primera fila y ultima columna', data2.iloc[0][2])
print('Valores de la primera fila:')
print(data2.iloc[0])


