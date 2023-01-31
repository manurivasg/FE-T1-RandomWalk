from tabulate import tabulate as tb
from mpl_toolkits import mplot3d
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


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
RETORNA:
Xf(np.array) : Arreglo con todas las posiciones de la caminata con la misma cantidad
                de columnas como dimensiones y filas como pasos se hayan ingresado por
                parámetro.
"""
def RandomWalk(dim,N):
    if 0<dim<4:
        X0 = np.array([[0]]*dim)#Se define una posición inicial
        DX = np.random.normal(0,1,(dim,N))#Se determinan las variaciones de posición bajo una dist. normal
        Xf = np.concatenate((X0,np.cumsum(DX, axis = 1)), axis = 1)#Se unen ambos arrays (X0,DX)
        # para el segundo array usamos cumsum que va sumando los valores anteriores 
        # con el siguiente para obtener la caminata
        
        if dim==1:#para una dimension muestra una tabla
            text = np.array([["Punto","Posición"]])
            for i in range(N):
                np.append("X"+str(i))
            table = np.concatenate((text,Xf),axis=1)
            print(tb(table,headers="firstrow",tablefmt="simple"))
        elif dim==2:#para 2 y 3 muestra una gráfica y guarda la figura 
            gr = plt.plot(Xf[0],Xf[1],"co-")
            plt.title("Random Walk",fontsize=14,fontweight="bold")
            plt.xlabel("Posición en coordenada X")
            plt.ylabel("Posición en coordenada Y")
            plt.savefig("random walk.jpg")
            plt.show()
        else: 
            fg = plt.figure(figsize=(10,8))
            axes = plt.axes(projection="3d")
            axes.scatter3D(Xf[0],Xf[1],Xf[2],color="cyan",marker="o")
            axes.plot3D(Xf[0],Xf[1],Xf[2],color="cyan")
            axes.set_title("Random Walk",fontsize=14,fontweight="bold")
            axes.set_xlabel("Posición en coordenada X")
            axes.set_ylabel("Posición en coordenada Y")
            axes.set_zlabel("Posición en coordenada Z")
            plt.savefig("random walk.jpg")
        return Xf

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
    print("Bienvenido a Random Walk Simulation")
    dim = int(input("Por favor ingrese las dimensiones en las que desea llevar a cabo la caminata aleatoria: (1-3) "))
    N = int(input("Por favor ingrese la cantidad de pasos que desea que tenga la caminata aleatoria: (>0) "))
    if 0<dim<4 and N>0:
        Xf = RandomWalk(dim,N)
        return Xf
    else: 
        print("No son válidos los parámetros que ingresa por input")
        return None

ejecutar_RandomWalk()