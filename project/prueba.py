import pandas as pd
import requests
from lxml import html
import matplotlib.pyplot as plt

#!Solo hago pruebas aqui

dfinter =pd.read_csv("python0123//project/dolarhistory.csv",sep = ";")
#print(dfinter)
#dfinter['dolar_venta','dolar_fecha'].plot()
plt.plot(dfinter['dolar_fecha'],dfinter['dolar_venta'])
plt.show()
#dfinter = dfinter['dolar_venta'].plot(kind= "bar")
#print(dfinter)
