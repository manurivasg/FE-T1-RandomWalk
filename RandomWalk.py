from tabulate import tabulate as tb
from mpl_toolkits import mplot3d
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from tqdm import tqdm, trange
import time




"""
Esta función recibe como parámetro de entrada un número de dimensiones y 
la cantidad de pasos que se quiere que tenga la caminata aleatoria 
y retorna un gráfico(2 y 3) o tabla (1), dependiendo de las 
dimensiones que se ingresen como parámetro, para visualizar los 
resultados. 

PARÁMETROS:
dim(int) : Número de dimensiones en las que se desea que se desea tener 
            la caminata aleatoria de la partícula (deben ser mayores a 0
            y menores a 3).
N(int) : Número de pasos que se desea que tenga la caminata aleatoria (es decir
            la cantidad total de variaciones que se le van a hacer a la posición
            inicial).
graph(bool) : Indica si se desea observar la gráfica de la caminata a reaizar

RETORNA:
Xf(np.array) : Arreglo con todas las posiciones de la caminata con la misma cantidad
                de columnas como dimensiones y filas como pasos se hayan ingresado por
                parámetro.
"""
def RandomWalk(dim,N,graph):
    if 0<dim<4:
        X0 = np.array([[0]]*dim)#Se define una posición inicial
        DX = np.random.normal(0,1,(dim,N))#Se determinan las variaciones de posición bajo una dist. normal
        Xf = np.concatenate((X0,np.cumsum(DX, axis = 1)), axis = 1)
        #Se unen ambos arrays (X0,DX)
        # para el segundo array usamos cumsum que va sumando los valores anteriores 
        # con el siguiente para obtener la caminata
        
        if dim==1 and graph:#para una dimension muestra una tabla
            for j in range(N):
                print("X"+str(j)+" | ",Xf[0][j],"\n")
        elif dim==2 and graph:#para 2 y 3 muestra una gráfica y guarda la figura 
            gr = plt.plot(Xf[0],Xf[1],"co-")
            plt.title("Random Walk",fontsize=14,fontweight="bold")
            plt.xlabel("Posición en coordenada X")
            plt.ylabel("Posición en coordenada Y")
            plt.savefig("random walk.jpg")
            plt.show()
        elif dim==3 and graph: 
            fg = plt.figure(figsize=(10,8))
            axes = plt.axes(projection="3d")
            axes.scatter3D(Xf[0],Xf[1],Xf[2],color="cyan",marker="o")
            axes.plot3D(Xf[0],Xf[1],Xf[2],color="cyan")
            axes.set_title("Random Walk",fontsize=14,fontweight="bold")
            axes.set_xlabel("Posición en coordenada X")
            axes.set_ylabel("Posición en coordenada Y")
            axes.set_zlabel("Posición en coordenada Z")
            plt.show()
            plt.savefig("random walk.jpg")
        return Xf

"""
Esta función desarrolla una serie de caminatas aleatorias todas bajo las mismas condiciones,
posteriormente calcula el vector de posición final para cada una de las caminatas y crea un
gráfica de barras que ilustra cuantas veces se repite cada posición final tras un gran 
número de repeticiones

PARÁMETROS: 
n(int) : Número de veces que se van a realizar las caminatas aleatorias. 
dim(int) : Número de dimensiones en las que se desea que se desea tener 
            la caminata aleatoria de la partícula (deben ser mayores a 0
            y menores a 3).
N(int) : Número de pasos que se desea que tenga la caminata aleatoria (es decir
            la cantidad total de variaciones que se le van a hacer a la posición
            inicial).

RETORNA: 
r(np.array) : Arreglo de las posiciones finales de las n repeticiones de caminatas
                aleatorias sin modificación alguna.
rf(np.array) : Arreglo de las posiciones finales de las n repeticiones de caminatas 
                aleatorias sin posiciones repetidas.
height(np.array) : Arreglo que almacena el número de veces que cada posición final
                    se repite en el arreglo inicial r.
"""
def RandomWalks_y_graph_r(n,N,dim):
    if dim == 1: 
        r = []
        for i in range(n):
            xf = RandomWalk(dim,N,graph=False)
            vec_r = round(np.sqrt(((xf[-1][0])**2)+((xf[-1][1])**2)),2)
            r.append(vec_r)
        height = count_occurrences(r)
        plt.bar(r,height,color="cyan",linewidth=0.1)
        plt.title("Número de veces que se repiten las distancias finales de la caminata aleatoria",fontsize=10,fontweight="bold")
        plt.xlabel("Distancias r")
        plt.ylabel("Repeticiones de cada distancia final")
        plt.savefig("repite each r.jpg")
        plt.show()
    elif dim == 2:
        r = []
        for i in range(n):
            xf = RandomWalk(dim,N,graph=False)
            vec_r = round(np.sqrt(((xf[-1][0])**2)+((xf[-1][1])**2)),2)
            r.append(vec_r)
        height = count_occurrences(r)
        
        plt.bar(r,height,color="cyan",linewidth=0.1)
        plt.title("Número de veces que se repiten las distancias finales de la caminata aleatoria",fontsize=10,fontweight="bold")
        plt.xlabel("Distancias r")
        plt.ylabel("Repeticiones de cada distancia final")
        plt.savefig("repite each r.jpg")
        plt.show()
    elif dim == 3:
        r = []
        for i in range(n):
            xf = RandomWalk(dim,N,graph=False)
            vec_r = round(np.sqrt(((xf[-1][0])**2)+((xf[-1][1])**2)+((xf[-1][2])**2)),2)
            r.append(vec_r)
        height = count_occurrences(r)
        plt.bar(r,height,color="cyan",linewidth=0.1)
        plt.title("Número de veces que se repiten las distancias finales de la caminata aleatoria",fontsize=10,fontweight="bold")
        plt.xlabel("Distancias r")
        plt.ylabel("Repeticiones de cada distancia final")
        plt.savefig("repite each r.jpg")
        plt.show()
    return r,height

"""
Esta función está encargada de calcular la cantidad de veces que se repite un 
eleento de una lista dentro de ella. 

PARÁMETROS:
r(np.array) : Arreglo al que se le quieren contar la cantidad de ocurrencias de 
                cada elemento y eliminarlo los elementos repetidos.

RETORNA: 

occurrences(np.array) : Arreglo con la cantidad de veces que se repite cada 
                        elemento en la lista original.
"""    
def count_occurrences(r):
    occurrences = []
    for i in range(len(r)):
        counter = 1
        for j in range(len(r)):
            if r[i] == r[j] and j != i:
                counter += 1
        occurrences.append(counter)

    return occurrences


"""
Esta función busca solicitarle al usuario por consola los datos necesarios para poder 
ejectuar la función RandomWalk y ejecutarla permitiendole al usuario observar los 
resultados de la caminata aleatoria.

PARÁMETROS:
None

RETORNA:
Xf(np.array) : Arreglo con todas las posiciones de la caminata con la misma cantidad
                de columnas como dimensiones y filas como pasos se hayan ingresado por
                parámetro.
"""    
def ejecutar_RandomWalk ():
    dim = int(input("Por favor ingrese las dimensiones en las que desea llevar a cabo la caminata aleatoria: (1-3) "))
    N = int(input("Por favor ingrese la cantidad de pasos que desea que tenga la caminata aleatoria: (>0) "))
    if 0<dim<4 and N>0:
        Xf = RandomWalk(dim,N,graph=True)
        return Xf
    else: 
        print("No son válidos los parámetros que ingresa por input")
        return None


"""
Esta función busca solicitarle al usuario por consola los datos necesarios para poder 
ejectuar la función RandomWalks_y_graph_r y ejecutarla permitiendole al usuario observar 
los resultados de la caminata aleatoria.

PARÁMETROS:
None

RETORNA:
r(np.array) : Arreglo de las posiciones finales de las n repeticiones de caminatas
                aleatorias sin modificación alguna.
rf(np.array) : Arreglo de las posiciones finales de las n repeticiones de caminatas 
                aleatorias sin posiciones repetidas.
height(np.array) : Arreglo que almacena el número de veces que cada posición final
                    se repite en el arreglo inicial r.
"""   
def ejecutar_RandomWalks_y_graph_r ():
    dim = int(input("Por favor ingrese las dimensiones en las que desea llevar a cabo la caminata aleatoria: (1-3) "))
    N = int(input("Por favor ingrese la cantidad de pasos que desea que tenga la caminata aleatoria: (>0) "))
    n = int(input("Ingrese el número de veces que desea que se repita el proceso: "))
    if 0<dim<4 and N>0 and n>0:
        r,h = RandomWalks_y_graph_r(n,N,dim)
        return r,h
    else: 
        print("No son válidos los parámetros que ingresa por input")
        return None

"""
Menú principal
"""
while(True):
    print("\nBienvenido a Random Walk Simulation\n")
    print("Menú Principal")
    print("1. Ejecutar una sola caminata aleatoria")
    print("2. Ejecutar N caminatas aleatorias con un N y dim constantes")
    print("3. EXIT")
    option = int(input("Ingrese la opción que desea probar: "))
    if option == 1: 
        xf = ejecutar_RandomWalk()
    elif option == 2:
        r,h = ejecutar_RandomWalks_y_graph_r()
    else: 
        print("¡Hasta Luego! :)")
        break
