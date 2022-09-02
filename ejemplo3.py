import pandas as pd
import numpy as np

archivo = pd.read_csv('Ventas.csv')
data = pd.DataFrame(archivo)
print(data)