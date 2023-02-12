import pandas as pd
import os
import db

message="""
    1)Insertar data:
    2)Actualizar data del dolar
    3)Mostrar grafica
    
    0)Cerrar
"""
print(message) 

def insertData():
    #obtiene la ruta absoluta
    path_=os.getcwd()+'\python0123\project\dataTienda.csv'
    
    #conection a bd
    conn=db.Conection(path_)
    cursor=conn.getCursor()
    print(path_)
    df = pd. read_csv (path_, sep = ";") 
    ### logica para insertar 
    for i,fila in df.iterrows():
        print(fila['NAME'])

def updateDolar():
    import requests
    from lxml import html
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' #tipo cambio sunat
    response = requests.get(url)
    data = response.json()
    data_venta = data["venta"]
    data_compra = data["compra"]
    data_fecha = data["fecha"]  #*Importando  data del dolar

    df = pd.DataFrame({'dolar_venta': [data_venta],'dolar_compra' : [data_compra],'dolar_fecha' : [data_fecha]})
    print(df)
    df.to_csv("python0123//project/dolarhistory.csv",";",mode="a",header=False,index= False) 
    #print(df) #*Actualizando data del dolar

    dfinter =pd.read_csv("python0123//project/dolarhistory.csv",sep = ";")
    dfinter = dfinter.tail()
    print(dfinter)#*Imprimiendo tabla con la nueva data guardada 
    print("Se actualizo la data del dolar")

def graficDolar():
    import matplotlib.pyplot as plt
    dfinter =pd.read_csv("python0123//project/dolarhistory.csv",sep = ";")
    plt.plot(dfinter['dolar_fecha'],dfinter['dolar_venta'])
    plt.show()

while True: 
    try:
        a=input('ingrese la tarea a realizar: ')
        if a.isnumeric : 
            a = int(a)
        if a == 1 :
            insertData()
            #break
        elif a == 2 :
            updateDolar()
            #break
        elif a == 3 :
            graficDolar()
            #break
        elif a == 0 :
            break
        else:
            print("ERROR. INTENTE DENUEVO")
    except Exception as a:
        print(a)