import pandas as pd
import requests
from lxml import html
import matplotlib.pyplot as plt

#!Solo hago pruebas aqui

dfinter =pd.read_csv("python0123//project/dataTienda.csv",sep = ";")
""" plt.plot(dfinter['dolar_fecha'],dfinter['dolar_venta'])
plt.show() """
#dfinter = dfinter['dolar_venta'].plot(kind= "bar")
print(dfinter)
