import funciones as fn
nombre=[]
edad=[]
rut=[]
fechanac=[]
oro=[]
plata=[]
bronce=[]
celular=[]
nombrepareja=[]
correo=[]
opc=0

while opc!=4:
    print ("-"*50)
    print ("1-Guardar datos")
    print ("2-Buscar participante en especifico")
    print ("3-Buscar e imprimir parejas")
    opc=int(input("ingrese la opcion deseada: "))
    if opc==1:
        fn.agregarcomp(nombre, edad, rut, fechanac, oro, plata, bronce, celular, nombrepareja, correo)
    elif opc==2:
        fn.buscarpart
    elif opc==3:
        

    else:
        fn.salir



