def registroDecoders():
    nombres=[]
    meses=[]
    grupos=[]
    edades=[]
    cedulas=[]

    fin= False
    while fin == False:
        nombre = input("nombre del estudiante: ")
        mes=input("mes de ingreso del estudiante: ")
        grupo=input("grupo asignado al estudiante: ")
        edad =input("edad del estudiante: ")
        cedula=input("documento del estudiante: ")

        nombres.append(nombre);meses.append(mes);grupos.append(grupo);edades.append(edad);cedulas.append(cedula)

        cierre= input("desea garegar a otro estudiante? y(sì) no(n)")
        if cierre == "n":
            fin = True
    listadeDatos=[]
    listadeDatos.append(nombres);listadeDatos.append(meses);listadeDatos.append(grupos);listadeDatos.append(edades);listadeDatos.append(cedulas)

    return listadeDatos

def asistencia(listaEstudiante=[]):
    asistencia={}
    cierre=False
        
    #registrode asistencia
    while cierre ==False:


        cedula=input("cedula del estudiante ")
        faltas=int(input("numero de faltas"))
        asistencia[cedula]=faltas

        fin= input("desea agregar asistencia a  otro estudiante? y(sì) no(n)")
        if fin == "y":
            cierre = False
        else:
            cierre = True
            break    

    return asistencia        

def eliminarEstudiantes(disccionario={},nombres=[],meses=[],grupos=[],edades=[],listaDeCedulas=[]):

    nuevaListaDeEstudiantes=[]
    disccionario=asistencia(listaDeCedulas)

    for identidad in  disccionario:
        if disccionario[identidad]>=15:
            indice = listaDeCedulas.index(identidad)

            listaDeCedulas.remove(listaDeCedulas[indice])
            nombres.remove(nombres[indice])
            meses.remove(meses[indice])
            grupos.remove(grupos[indice])
            edades.remove(edades[indice])

    nuevaListaDeEstudiantes.append(nombres);nuevaListaDeEstudiantes.append(meses);nuevaListaDeEstudiantes.append(grupos);nuevaListaDeEstudiantes.append(edades);nuevaListaDeEstudiantes.append(listaDeCedulas)

    return nuevaListaDeEstudiantes                


def duplicados(lista1=[],lista2=[]):
    lista3=[]
    for nombre in lista1:
         
         if nombre in lista2:
             lista3.append(nombre)

    return lista3        


def listarCoders(listaDeCoders=[]):
    #recibe la lista de registro de coders


    nombres=listaDeCoders[0]
    meses=listaDeCoders[1]
    grupos=listaDeCoders[2]
    edades=listaDeCoders[3]
    cedulas=listaDeCoders[4]

    for i in range(len(nombres)):
        print("|",nombres[i],"|",meses[i],"|",grupos[i],"|",edades[i],"|",cedulas[i],"|")


def cambioDeEstudiante(destino="",lista1=[],lista2=[]):

    arregloFinal=[] #este arreglo tendrá las listas finales ya modificadas

    #la lista1 es en donde está el estudiante y la lista2 es en donde se quire reubicar

    #usuarios de la primera lista
    nombres1=lista1[0]
    meses1=lista1[1]
    grupos1=lista1[2]
    edades1=lista1[3]
    cedulas1=lista1[4]
    #usuarios de la segunda lista
    nombres2=lista2[0]
    meses2=lista2[1]
    grupos2=lista2[2]
    edades2=lista2[3]
    cedulas2=lista2[4]
    #_________________________________________________

    identificacion=input("identificacion del esudiante que desea hacer el cambio: ")
    indice=cedulas1.index(identificacion)#tengo el indice de la posiscion del estudiante en la lista
    #datos del estudiante a cambiar
    nombre=nombres1[indice]
    mes=meses1[indice]
    grupo=destino
    edad=edades1[indice]
    cedula=cedulas1[indice]
    #__________________________________

    nombres1.pop(indice)
    nombres2.append(nombre)

    meses1.pop(indice)
    meses2.append(mes)

    
    grupos1.pop(indice)
    grupos2.append(grupo)
    

    

    edades1.pop(indice)
    edades2.append(edad)

    cedulas1.pop(indice)
    cedulas2.append(cedula)

    lista1.append(nombres1);lista1.append(meses1);lista1.append(grupos1);lista1.append(edades1);lista1.append(cedulas1)
    lista2.append(nombres2);lista2.append(meses2);lista2.append(grupos2);lista2.append(edades2);lista2.append(cedulas2)

    arregloFinal.append(lista1);arregloFinal.append(lista2)

    return arregloFinal  
    











    