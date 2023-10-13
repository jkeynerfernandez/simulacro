def registroDecoders():
    nombres=[]
    meses=[]
    grupos=[]
    edades=[]

    fin= False
    while fin == False:
        nombre = input("nombre del estudiante: ")
        mes=input("mes de ingreso del estudiante: ")
        grupo=input("grupo asignado al estudiante: ")
        edad =input("edad del estudiante: ")
        
        nombres.append(nombre);meses.append(mes);grupos.append(grupo);edades.append(edad)

        cierre= input("desea garegar a otro estudiante? y(sì) no(n)")
        if cierre == "n":
            fin = False
    listadeDatos=[]
    listadeDatos.append(nombres);listadeDatos.append(meses);listadeDatos.append(grupos);listadeDatos.append(edades)

    return listadeDatos


def duplicados(lista1=[],lista2=[]):
    lista3=[]
    for nombre in lista1:
         
         if nombre in lista2:
             lista3.append(nombre)

    return lista3         
    