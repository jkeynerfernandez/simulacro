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


    