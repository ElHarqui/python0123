import controller as ctr

message="""
    1)Insertar un usuario
    2)ver lista de usuarios
    3)buscar usuario
"""
global option
option=input('ingrese una opcion: ')

def registerUser():
    usuario=input('ingrese el siguiente data usuario: ')
    password=input('ingrese el siguiente data password: ')
    email=input('ingrese el siguiente data email: ')
    fullname=input('ingrese el siguiente data fullname: ')
    tipousuario=input('ingrese el siguiente data tipousuario: ')
    data=(usuario,password,email,fullname,tipousuario)
    try:
        ctr.insertUser(data)
    except Exception as e:
        print("error al ingresar data")
        print(e)
def listUser():
    data=ctr.controllerUser()
    for row in data:
        print(row)

if __name__=='__main__':
    if option=='1':
        registerUser()
        listUser()


