import pandas as pd

ventas2021 = {'MESES':['Enero','Febrero','Marzo','Abril','Mayo','Junio'],
          'MONTO':[55000,60000,67000,25000,45000,38000]}
ventas2022 = {'MESES':['Enero','Febrero','Marzo','Abril','Mayo','Junio'],
          'MONTO':[85000,70000,25000,45000,85000,72000]}

data1 = pd.DataFrame(ventas2021)
data2 = pd.DataFrame(ventas2022)

datos = data1.add(data2)

print(data1)
print(data2)
print(datos)