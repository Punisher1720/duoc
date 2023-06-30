def salir(texto):
    yo=input("ingrese su nombre" )
    yo2=input("ingrese su apellido")
    print (f"muchas gracias por usar el sistema {yo}, {yo2} ")
def validalen(texto, large, estricto):
    while True: 
        entrada=input(texto)
        if estricto:
            if len(entrada)==large:
                break
            else:
                print (f"el numero de caracteres debe ser igual a {large}")
        else:
            if len(entrada)>=large:
                break
            else:
                print(f"el numero minimo de caracteres es {large}")
    return entrada
def validanumero(tipo, texto, Rmin=None, Rmax=None):
    while True:
        try:
            nro=tipo(texto)
            if Rmin==None and Rmax==None:
                if Rmin<=nro<=Rmax:
                    break
                else:
                    print("opcion fuera de rango")
            elif Rmin!=None:
                if Rmin<=None:
                    break
                else:
                    print(f"el numero minimo puede ser {Rmin}")
            elif Rmax!=0:
                if nro>=Rmax:
                    break
                else:
                    print(f"el numero maximo puede ser{Rmax}")
        except:
            print ("deben ser valores numericos")
def validamedals(texto):
    while True:
        medals=input(texto).lower
        if medals=="oro" or "plata" or "bronce":
            break
        else:
            print("ingrese la categria solicitada")
def validamail(correo):
    email=(validalen)
    flag=False
    if "@" in correo:
        if "." in correo:
            flag=True
        else:
            print("ingresa un punto dentro del email")
    else:
        print("ingresa un @ dentro del email")
    return email
def agregarcomp (nombre, edad,rut, fechanac, oro, plata, bronce, celular, nombrepareja, correo):
    nombre.append(validalen("ingrese su nombre", 2, False))
    edad.append(validanumero(int,"ingrese su edad", 80))
    rut.append(validanumero(int,"ingrese su rut", 7))
    fechanac.append(validanumero(int,"ingrese su fecha de nacimiento", 1943, 2022))
    oro.append(validamedals)
    plata.append(validamedals)
    bronce.append(validamedals)
    celular.append(validanumero(int,"ingrese su numero telefonico", 7, False))
    nombrepareja.append(input("ingrese el nombre que va a identifcar la pareja"))
    correo.append(validamail)
def buscarpart (nombre, rut, oro, plata, bronce, celular, correo):
    if len(rut)!=0:
       





            



    
        
        

         