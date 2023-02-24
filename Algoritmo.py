import csv
import os
import time
from os import system

folder = 'C:\\Users\\HP\\Documents\\IA-Tarea3\\'    #   DIRECCION DEL FOLDER "low-dimensional"
datos = []
kmin = 1

system("cls") #LIMPIA LA TERMINAL

#LEE LAS INSTANCIAS DEL ARCHIVO
def asignar_Instancias(filename):
   print(' ____________________________________________________'+filename+' ____________________________________________________')
   nodo = []
   peso = []
   beneficio = []
   capacidad = []
   n = 0
   with open(folder+ 'low-dimensional\\' + filename, 'rt') as f:
      reader = csv.reader(f)
      peso.append("0")
      beneficio.append("0")
      nodo.append(n)
      for row in reader:
         if(len(row)>0):
            if(row[0] != ''):
               n += 1
               nodo.append(n)
               peso.append(row[0])
               beneficio.append(row[1])
               if(row[2] != ''):
                capacidad.append(row[2])
   return(list([nodo, peso, beneficio, capacidad]))

def beneficio_peso(datos):

    valor_h = [0]

    for nodos in range(1, len(datos[0]), 1):
        
        valor_h.append(float(datos[1][nodos]) + float(datos[2][nodos]))

    return valor_h

def algoritmo(valor_h, datos):
    
    capacidad_Maxima = float(datos[3][0])     #   CAPACIDAD MAXIMA DEL PROBLEMA
    nodos_Factibles = []                    #   NODOS QUE YA SE VISITARON Y SON FACTIBLES
    nodos = datos[0]                        #   NODOS QUE AUN NO SE VISITAN
    nodo_Aceptado = 0                       #   NODO ACEPTADO EN LA ITERACION
    iteraciones = len(datos[0])             #   NO. DE ITERACIONES POSIBLES DE HACER
    capacidad_Actual = 0                    #   OBTENER LA CAPACIDAD QUE TENEMOS DURANTE LA EJECUCION
    beneficio = 0                           #   BENEFICIO AL MOMENTO

    #VERIFICA SI YA PASO DE LA CAPACIDAD
    if(capacidad_Maxima <= capacidad_Actual):
            
        #TERMINA EL ALGORITMO
        return (list([capacidad_Actual, beneficio, nodos_Factibles]))
    
    nodos_Factibles.append(datos[0][0])     #   AGREGA EL NODO 0 COMO FACTIBLE
    nodos.pop(0)                            #   ELIMINA EL NODO 0 DE LOS NODOS DISPONIBLES

    #VISITA TODOS LOS NODOS POSIBLES
    for mov_Nodos in range(0, iteraciones, 1):
        
        #VERIFICA SI SE PUEDE MOVER AL NODO
        for iteracion in range (0, len(nodos),1):
            
            #CHECA SI NO SE PASA DE LA CAPACIDAD Y SI TIENE MAS VALOR h(x) AL NODO ACEPTADO
            if(((float(datos[2][nodos[iteracion]]) + capacidad_Actual) <= capacidad_Maxima) and
               (valor_h[nodos[iteracion]] > valor_h[nodo_Aceptado])):
                
                nodo_Aceptado = nodos[iteracion]
        
        #VERIFICA SI SE ENCONTRO UN NODO FACTIBLE
        if(nodo_Aceptado != 0):

            #AGREGA EL NODO A LA LISTA DE NODOS FACTIBLES
            nodos_Factibles.append(nodo_Aceptado)

            #ELIMINA EL NODO ACEPTADO DE LOS NODOS DISPONIBLES
            nodos.remove(nodo_Aceptado)

            #HACE LA SUMA DEL BENEFICIO Y LA CAPACIDAD DEL NODO ACEPTADO
            beneficio += float(datos[1][nodo_Aceptado])
            capacidad_Actual += float(datos[2][nodo_Aceptado])

            #IMPRIME RESUMEN DE LA ITERACION
            #print("Nodo Actual: " + str(nodo_Aceptado) + "      Beneficio: " + str(beneficio) + "       Capacidad: " + str(capacidad_Actual))

            #REINICIA EL NODO PARA LA NUEVA ITERACION
            nodo_Aceptado = 0
            
        else:

            #REGRESA LOS VALORES FACTIBLES
            return (list([capacidad_Actual, beneficio, nodos_Factibles]))


    #TERMINA EL ALGORIMO
    return (list([capacidad_Actual, beneficio, nodos_Factibles]))

#REALIZA n ITERACIONES
for iteraciones in range(1,10,1):
    for filename in os.listdir(folder + 'low-dimensional\\'):
        if filename.endswith(".csv"):
            nombre = filename.split('_')
            datos = asignar_Instancias(filename) #PASAMOS LAS INSTANCIAS A UNA VARIABLE
            start_time = time.time()
            resultado = algoritmo(beneficio_peso(datos), datos)
            #print("-------------------------------------------------------------------------")
            runtime = time.time() - start_time
            print("Capacidad: " + str(resultado[0]) + "      Beneficio: " + str(resultado[1]) + "       Nodos: "
                  + str(resultado[2]) + "        Runtime: " + str(runtime))
            datos = []
