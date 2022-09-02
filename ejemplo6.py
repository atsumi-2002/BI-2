import pandas as pd
archivo = pd.read_excel('Ventas02.xlsx',sheet_name='Ventas',skiprows=1)
data = pd.DataFrame(archivo)
print(data)