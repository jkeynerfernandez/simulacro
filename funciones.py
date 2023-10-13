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

    #___________________________________
    #agregar estudiantes al diccionario

    for estudiante in listaEstudiante:
        asistencia[estudiante]=None
    #____________________________________    
    #registrode asistencia
    while cierre ==False:


        cedula=input("cedula del estudiante ")
        faltas=input("numero de faltas")
        asistencia[cedula]=faltas

        fin= input("desea garegar a otro estudiante? y(sì) no(n)")
        if fin == "n":
            cierre = True
    return asistencia        

        






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


    