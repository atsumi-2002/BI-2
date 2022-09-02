import pandas as pd
import numpy as np

ventas = {'MESES':['Enero','Febrero','Marzo','Abril','Mayo','Junio'],
          'MONTO':[55000,60000,67000,25000,45000,38000]}
data1 = pd.DataFrame(ventas)
print(data1)
data2 = pd.DataFrame(ventas,columns=['MONTO','MESES'])
print(data2)