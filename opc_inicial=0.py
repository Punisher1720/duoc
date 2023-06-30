opc_inicial=0
total=0
cont=0
pordesc=0
descuent=0
while opc_inicial!=3:
    print ("1. cotizacion")
    print ("2. reiniciar cotizacion")
    print ("3. salir")
    while True:
        try:
            opc_inicial=int(input("ingrese una opcion: (dentro del rango 1, 2 y 3) "))
            if 1<=opc_inicial<=3:
                break
            else:
                print("ingrese una opcion valida!!!")
        except:
            print("ingrese una opcion numerica")
    if opc_inicial==1:
            
            opc_tratamiento=0
            while opc_tratamiento!=4:
                print ("1. Carillas Porcelana")
                print ("2. Implantes Dentales")
                print ("3. Ortodoncia Brackets")
                print ("4. salir, hacer descuento y cotizacion correspondiente")
                while True:
                     
                    try:
                        opc_tratamiento=int(input("ingrese el tratamiento que desea: "))
                        if 1<=opc_tratamiento<=4:
                            break
                        else:
                            print("ingrese una opcion valida!!!")
                    except:
                        print("ingrese una opcion numerica")
                    
                if opc_tratamiento==1:
                        total+=250000
                        cont+=1
                elif opc_tratamiento==2:
                        total+=475000
                        cont+=1
                elif opc_tratamiento==3:
                        total+=800000
                        cont+=1
                
                else:
                    while True:
                        try:
                            descuento=int(input("elija si tiene algun oficio de los que se presentan:\n 1. trabajador auxiliar\n 2. trabajador administrativo\n 3. trabajador docente\n 4. no tengo descuento "))
                            if 1<=descuento<=4:
                                break
                            else:
                                print ("ingrese un numero dentro del rango")
                        except:
                            print ("ingrese un numero y no una letra")
                    if descuento==1:
                                descuent= total*0.15
                                pordesc=15
                                rialdiscount=total-(total*0.15)
                    elif descuento==2:
                                descuent= total*0.1
                                pordesc=10
                                rialdiscount=total-(total*0.1)
                    elif descuento==3: 
                                descuent= total*0.05
                                pordesc=5
                                rialdiscount=total-(total*0.05)
                    
                    else:
                                descuent= 0
                                pordesc=0
                                rialdiscount=total
                         
                        
                    print ("-------------------------------------")
                    print ("            Cotizacion:              ")
                    print (f"{cont} tratamientos solicitados ")
                    print (f"subtotal: {total}")
                    print (f"descuento: {pordesc} ")
                    print ("-------------------------------------")
                    print (f"Total: {total}")
                    print ("-------------------------------------")
                    print (f"son 12 cuotas de : {total//12}")
                    print ("\nSonria bonito!!!!!")                
                    
    elif opc_inicial==2:
        print (f"la cotizacion total fue: {total}")
        total=0
        cont=0
    else:
        print ("adios y gracias por comprar con nosotros")



                    
                    
                    

    
        




