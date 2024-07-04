import csv
'''
DATOS DEL ARCHIVO:
Esteban:Gutierrez:4.9:1.8:3.2
Luisa:Miranda:6.8:4.4:5.6
Jean Paul:Munoz:4.8:3.8:2.1
Gianfranco:Basso:5.4:5.4:5.0
Romina:Smith:1.0:2.8:5.9
'''
aprobados = []
reprobados = []

def Abrir_archivo():
    datos = []
    with open("alumnos.txt", "r", newline="") as arch: #Abro el archivo "alumnos.txt" como lectura 
        for linea in arch: #Itero de una en una, las lineas del archivo
            Linea = linea.strip().split(":") #Hago una lista separando los elementos de la linea por los (:)
            datos.append(Linea) #Creo la sublista que tendra todos los datos de los alumnos
        convertir_nums(datos)
    return datos

def convertir_nums(d):
    #Itero sobre la lista bidimensional
    for E in d:
        #Itero sobre cada una de las listas
        for i in range(len(E[2:])): #i en rango del largo de la lista (desde la posicion 2 hasta el final -> se hara el ciclo 3 veces)
            E[i+2] = float(E[i+2]) #-> cambio la posicion i+2 de la lista de tipo (de str a float)
            #i empezara como 1, y finalizara en el 3
    #Resultando en el cambio de tipo de la variable

def escribir_archivos():
    with open("aprobados.csv", "w") as Archivo:
        Archivo.write("Nombre, Apellido\n")
        for A in aprobados:
            Archivo.write(A[0]+","+A[1]+"\n")

    A_Reprobados = open("reprobados.csv","w")
    A_Reprobados.write("Nombre, Apellido\n")
    for A in reprobados:
        A_Reprobados.write(A[0]+","+A[1]+"\n")
    A_Reprobados.close()



# ***** MAIN *****
Alumnos = Abrir_archivo()

#Itero sobre la lista bidimensional
for E in Alumnos:
    #Itero sobre cada una de las listas
    for i in range(len(E[2:])): #i en rango del largo de la lista (desde la posicion 2 hasta el final -> se hara el ciclo 3 veces)
        E[i+2] = float(E[i+2]) #-> cambio la posicion i+2 de la lista de tipo (de str a float)
        #i empezara como 1, y finalizara en el 3
#Resultando en el cambio de tipo de la variable


for n in Alumnos: #n => lista (como elemento de la sublista)
    if round(sum(n[2:])/len(n[2:]),2) >= 4: #Pregunto si el promedio es >= 4
        aprobados.append(n[:2])
    else:
        reprobados.append(n[:2])

print(aprobados) #estos prints son para asegurarme de que todo va bien 
print(reprobados)

escribir_archivos()