import pandas as pd
import requests
from lxml import html
url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
response = requests.get(url)
data = response.json()
data_venta = data["venta"]
data_compra = data["compra"]
data_fecha = data["fecha"]

df = pd.DataFrame({'dolar_venta': [data_venta],'dolar_compra' : [data_compra],'dolar_fecha' : [data_fecha]})
df.to_csv("python0123//project/dolarhistory.csv",";",mode="a",header=False,index= False) 
print(df)

dfinter =pd.read_csv("python0123//project/dolarhistory.csv")
dfinter = dfinter.tail(3)
print(dfinter)
#!Solo hago pruebas aqui