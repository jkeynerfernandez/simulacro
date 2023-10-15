from funciones import *
codersGrupoA=[["juan","keyner","fernandez"],["enero","febrero","marzo"],["a","a","a"],[18,19,20],["123","456","789"]]
codersGrupoB=[["gabriel","caldera","hincapie"],["enero","febrero","marzo"],["b","b","b"],[18,19,20],["987","654","321"]]
codersGrupoC=[["flor","milena","bola8"],["enero","febrero","marzo"],["c","c","c"],[18,19,20],["369","258","147"]]

cerrar=False
while cerrar == False:

    case=input("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")


    match case:
        case "1":
            grupo=input("grupo al que desea agregar estudiantes: (A)(B)(C)")
            match grupo:
                case "a":
                    codersGrupoA=registroDecoders()
                    listarCoders(codersGrupoA)
                    continuar=input("cerrar programa?: sì (y) no(n)")

                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")
                    
                case "b":
                    codersGrupoB=registroDecoders()
                    listarCoders(codersGrupoB) 
                    continuar=input("cerrar programa?: sì (y) no(n)")
                    
                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")

                case "c":
                    codersGrupoC=registroDecoders()
                    listarCoders(codersGrupoC)
                    continuar=input("cerrar programa?: sì (y) no(n)")
                    
                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")

        
        
        
        case "2":

            #para que este caso funcione tienen que existir las listas de grupos
            opcion1=input("primera lista: (A)(B)(C)")
            opcion2=input("segunda lista: (A)(B)(C)")

            if opcion1== "a":
                lista1=codersGrupoA
            elif opcion1 == "b":
                lista1=codersGrupoB
            else:
                lista1=codersGrupoB  


            if opcion2== "a":
                lista2=codersGrupoA
            elif opcion2 == "b":
                lista2=codersGrupoB
            else:
                lista2=codersGrupoB       

            listaDeCodersDuplicados=duplicados(lista1,lista2)
            print(listaDeCodersDuplicados)

            continuar=input("cerrar programa?: sì (y) no(n)")
                    
            if continuar == "y":
                cerrar = True
            else:    
                case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")


        case "3":
            grupo=input("grupo del estudiante a evaluar (A)(B)(C)")
            match grupo:

                case "a":
                    #antes de eliminar hay que registrar las FALTAS
                    faltas=asistencia(codersGrupoA) #faltas es un diccionario clave=cedulas y valor=numFaltas
                    #eliminarlos
                    
                    codersGrupoA=eliminarEstudiantes(faltas,codersGrupoA[0],codersGrupoA[1],codersGrupoA[2],codersGrupoA[3],codersGrupoA[4])
                    listarCoders(codersGrupoA)

                    continuar=input("cerrar programa?: sì (y) no(n)")
                    
                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")



                    
                case "b":

                    #antes de eliminar hay que registrar las FALTAS
                    faltas=asistencia(codersGrupoB) #faltas es un diccionario clave=cedulas y valor=numFaltas
                    #eliminarlos
                    
                    codersGrupoB=eliminarEstudiantes(faltas,codersGrupoB[0],codersGrupoB[1],codersGrupoB[2],codersGrupoB[3],codersGrupoB[4])
                    listarCoders(codersGrupoB)

                    continuar=input("cerrar programa?: sì (y) no(n)")
                    
                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")

                   
                case "c":
                    #antes de eliminar hay que registrar las FALTAS
                    faltas=asistencia(codersGrupoC) #faltas es un diccionario clave=cedulas y valor=numFaltas
                    #eliminarlos
                    
                    codersGrupoC=eliminarEstudiantes(faltas,codersGrupoC[0],codersGrupoC[1],codersGrupoC[2],codersGrupoC[3],codersGrupoC[4])
                    listarCoders(codersGrupoC)

                    continuar=input("cerrar programa?: sì (y) no(n)")
                    
                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")

        case "4":
            mostrar = input("lista del grupo que desea mostrat (A)(B)(C) Todos (T)")
            match mostrar:

                case "a":
                    listarCoders(codersGrupoA)
               
                    continuar=input("cerrar programa?: sì (y) no(n)")
                    
                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")
               
                case "b":
                    listarCoders(codersGrupoB)
             
                    continuar=input("cerrar programa?: sì (y) no(n)")
                    
                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")
             
                case "c":
                    listarCoders(codersGrupoC)

                    continuar=input("cerrar programa?: sì (y) no(n)")
                    
                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")
               
                case "t":
                    listarCoders(codersGrupoA)            
                    listarCoders(codersGrupoB)
                    listarCoders(codersGrupoC)

                    continuar=input("cerrar programa?: sì (y) no(n)")
                    
                    if continuar == "y":
                        cerrar = True
                    else:    
                        case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")

        case "5":
            listarCoders(codersGrupoA)            
            listarCoders(codersGrupoB)
            listarCoders(codersGrupoC)

            origen=input("lista de origen del estudiante: (A)(B)(C) ")
            destino=input("lista de destino del estudiante: (A)(B)(C) ")

            if origen=="a":
                listaOrigen=codersGrupoA
            elif origen=="b":
                listaOrigen=codersGrupoB
            else:
                listaOrigen=codersGrupoC

            if destino =="a":
                listaDestino=codersGrupoA
            elif destino=="b":
                listaDestino=codersGrupoB
            else:
                listaDestino=codersGrupoC

            cambioRealizado=cambioDeEstudiante(listaOrigen,listaDestino) #

            if origen=="a":
                codersGrupoA=cambioRealizado[0]
            elif origen=="b":
                codersGrupoB=cambioRealizado[0]
            else:
                codersGrupoC=cambioRealizado[0]

            if destino=="a":
                codersGrupoA=cambioRealizado[1]
            elif destino=="b":
                codersGrupoB=cambioRealizado[1]
            else:
                codersGrupoC=cambioRealizado[1]

            listarCoders(codersGrupoA)            
            listarCoders(codersGrupoB)
            listarCoders(codersGrupoC) 

            continuar=input("cerrar programa?: sì (y) no(n)")
                    
            if continuar == "y":
               cerrar = True
            else:    
                case=print("¿Que desea hacer?\n1.Agregar estudiantes\n2.Buscar coders duplicados en dos grupos\n3.eliminar coders por insistencia\n4.ver lista de estudiantes\n5.Cambiar estudiante de grupo\n")
              
           




            


            




