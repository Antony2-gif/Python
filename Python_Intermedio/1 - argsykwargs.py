"""
Como funciona *args
"""

def funcion1(argu_1, *argumentos):
    print("Argumento 1" + argu_1)
    for i in argumentos:
        print("Argumentos de args" ,i)

funcion1("Hola","Como","Estas")

"""
Uso de **kwars
- Permite pasar argumentos con un key a una funcion
"""

def funcion_kwars(**kwargs):
    for key,value in kwargs.items():
        print("{}->{}".format(key,value))

funcion_kwars(nombre = "Antonio")


"""
Usando *args y **kwargs
"""

def funcion3(arg,arg2,arg3):
    print("Argumento 1:" ,arg)
    print("Argumento 2:" , arg2)
    print("Argumento 3:" , arg3)



#Utilizado *args
tupla = (3,2,1)

funcion3(*tupla)

print("#"*20)
#Utilizadno **kwargs

kwars = {"arg3":3,"arg":1,"arg2":2}

funcion3(**kwars)
