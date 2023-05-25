cariPorcelana=250000
contCP=0
implaDentales=475000
contID=0
ortBrackets=800000
contOB=0
Tauxi=0.85
Tadmin=0.9
Tdocen=0.95
TTotal=0
desc=0
x=0
opc=0
opc1=0
while x!=3:
    opc1=0
    print(32*"-")
    print("Bienveido a Diente de Oro")
    print(32*"-")
    print()
    print("1) Comenzar Cotizacion")
    print("2) Renunciar cotizacion")
    print("3) Salir")
    print("")
    print(32*"-")
    print("")
    while True:
        try:
            x=int(input("Elija su opcio: "))
            if 1<=x<4:
                break
            else:
                print("valo fuera de rango")
        except ValueError:
            print("Introdusca un valor numerico")
    if x==1:
        if desc==0:
            while True:
                    print("")
                    print(32*"-")
                    print("")
                    print("Que tipo De trabajador es")
                    print("")
                    print("1) Trabajador Auxiliar")
                    print("2) Trabajador Administrativo")
                    print("3) Trabajador Docente")
                    print("4) Ninguno")
                    print("")
                    print(32*"-")
                    print("")
                    try:
                        opc=int(input("Selecione su opcion: "))
                        if 1<=opc<=4:
                            if opc==1:
                                desc=Tauxi
                                break
                            elif opc==2:
                                desc=Tadmin
                                break
                            elif opc==3:
                                desc=Tdocen
                                break
                            else:
                                desc=1
                                break
                        else:
                            print("opcion fuera de rango")
                    except ValueError:
        
                        print("orfavor introdusca un valor numerico")
        if desc>0:
            while opc1!=4:
                print("")
                print(32*"-")
                print("")
                print("Tratamientos disponibles")
                print("1) Carillas Porcelanas")
                print("2) Implantes Dentales")
                print("3) Ortodoncia Brackest")
                print("4) Salir")
                print("")
                print(f"Total actual {TTotal}")
                print(f"Total por planilla {TTotal/12}")
                print("")
                print(32*"-")
                print("")
                while True:
                    try:
                        opc1=int(input("Selecione su opcion: "))
                        if 1<=opc1<=4:
                            if opc1==1:
                                TTotal=TTotal+(cariPorcelana*desc)
                                contCP=contCP+1
                                break
                            elif opc1==2:
                                TTotal=TTotal+(implaDentales*desc)
                                contID=contID+1
                                break
                            elif opc1==3:
                                TTotal=TTotal+(ortBrackets*desc)
                                contOB=contOB+1
                                break
                            else:
                                break
                        else:
                            print("opcion fuera de rango")
                    except ValueError:
                        print("orfavor introdusca un valor numerico")               
            
    elif x==2:
        print("")
        print(32*"-")
        print("")
        print(f"Cotizacion Acutal {TTotal}\nTotal por Planilla {TTotal/12}")
        print("")
        print("opciones")
        print("1) Eliminar Cotizacion")
        print("2) Volver")
        print("")
        print(32*"-")
        print("")
        while True:
            try:
                opc2=int(input("Selecione su opcion: "))
                if opc2==1 or opc2==2:
                    if opc2==1:
                        TTotal=0
                        desc=0
                        contCP=0
                        contID=0
                        contOB=0
                        break
                    else:
                        break
                else:
                    print("opcion fuera de rango")
            except ValueError:
                print("Porfavor utilize un Valor numerico")
    else:
        TS=(cariPorcelana*contCP)+(implaDentales*contID)+(ortBrackets*contOB)
        print("Saliendo")
        print("")
        print(32*"-")
        print("")
        print("\tContizacones")
        print("")
        print(32*"-")
        print("")
        print(32*"-")
        print(f"-->{contCP} tratamiento(s) Carillas Porcelana {cariPorcelana*contCP}")
        print(f"-->{contID} tratamiento(s) Carillas Porcelana {implaDentales*contID}")
        print(f"-->{contOB} tratamiento(s) Carillas Porcelana {ortBrackets*contOB}")
        print(32*"-")
        print(f"Subtotal {TS}")
        print(f"Descuento:{1-desc}%   {(1-desc)*TS}")
        print(32*"-")
        print(f"Total {TTotal}")
        print(32*"-")
        print(f"Son 12 cuotas de {TTotal/12}")
        print("")
        print("Sonria Bonito")
    