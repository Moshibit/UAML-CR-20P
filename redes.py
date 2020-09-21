# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:46:05 2020

@author: Erik Juarez-Guerrero
"""

import matplotlib.pyplot as plt
import random

## Tarea 1 ####################################################################

def numero_nodos(red): 
    """
    Recibe un red y regresa el número de nodos de ella.    

    Parámetros
    ----------
    red : TIPO. diccionario
          DESCRIPCCCIÓN. Las claves representan los nodos y los valores son 
          conjunto de los nodos conectados.
          
    Excepción
    ---------
    TypeError
        Se lanza cuando no recibe un diccionario como parámetro

    Valor de retorno
    ----------------
    rv : entero
         El número de nodos de la red.

    """

    # valida el paramtro que recice la función
    if type(red) is not dict:
        raise TypeError("el parámetro que recibe numero_nodos() tiene que ser un diccionario")
        
    # mide la cantidad de nodos de la red
    rv = len(red)
    return rv
    

def calcula_grados(red):
    """
    Recibe una red y regresa un diccionario con los grados de cada nodo

    Parámetros
    ----------
    red : TIPO. diccionario
          DESCRIPCCCIÓN. Las claves representan los nodos y los valores son 
          conjunto de los nodos conectados.
          
    Excepción
    ---------
    TypeError
        DESCRIPTION. Cuando no resive un diccionario como paramátro
    
    Regreas
    -------
    rv : TIPO. Diccionario
         DESCRIPCCCIÓN. Las llaves representasn los nodos de la res y los 
         valores son el grado de entrada del nodo

    """
    
    # valida el paramtro que recice la funcion, puede lanzar una excepción
    if type(red) is not dict:
        raise TypeError("el parámetro que recibe numero_nodos() tiene que ser un diccionario")
    
    # Construlle un diccionario verificando el grado de los nodos de la red
    rv = { }
    for k, v in red.items():
        rv[k] = len(v)
    return rv


def grado_maximo(red):
    """
    Recibe una red y regresa la llave del nodo con mayor grado

    Parámetros
    ----------
    red : TIPO. diccionario
          DESCRIPCCCIÓN. Las claves representan los nodos y los valores son 
          conjunto de los nodos conectados.
          
    Excepción
    ---------
    TypeError
        DESCRIPTION. Cuando no resive un diccionario como paramátro
    
    Regreas
    -------
    rv : TIPO. entero
         DESCRIPCCCIÓN. el valor que tenga la llave de nodo con grado maxímo
    """
    # TODO: optimisar la función
    
    # valida el paramtro que recice la funcion, puede lanzar una excepción
    if type(red) is not dict:
        raise TypeError("el parámetro que recibe numero_nodos() tiene que ser un diccionario")
 
    # obtiene un diccionario con los grados de cada nodo
    d = calcula_grados(red)
    
    # busca en los valores del diccionario que valor es el máximo
    rv = max(d.values())   
    return rv


## Práctica 1 #################################################################

def crea_un_grafo_completo(n):
    """
    Resibe un número entero para regresar un grafo del tipo K_n.
    (todos los nodos estan relacionados entre ellos.)

    Parámetros
    ----------
    n : TIPO. entero mayor a cero
        DESCRIPCIÓN. Es el número de nodos del grafo.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Caundo no se pasa un entero por parámetro.
    ValueError
        DESCRIPCIÓN. Cuando el entero no es mayor a cero.

    Valor de retorno
    ----------------
    k_n : TIPO. diccionario
        DESCRIPCiÓN. Grafo K_n es un diccionario cuyos valores son conjuntos
        que representan los enlaces a otros nodos, cada elementp del conjunto
        es un nodo relacionado.

    """
    
    # validación del parámetro de entrada
    if type(n) is not int:
        raise TypeError("el parámetro que recibe crea_un_grafo_completo() tiene que ser un entero positivo.")
    if n < 1:
        raise ValueError("el parámetro que recibe crea_un_grafo_completo() tiene que ser mayor a cero.")
        
    # el grafo vacío
    k_n = { }
   
    # contrucción del grafo
    for i in range(n):
        
        # conjunto de nodos vacío, es el valor que se gurdará en la clave i 
        # en el diccionario
        ady = set()
        
        # se contruye el conjunto de nodos adyasentes
        for j in range(n):
            if i != j:
                ady.add(j)
        k_n[i] = ady
    
    return k_n


def calcula_grados_de_entrada(d_grafica):
    """
    Recibe un diccionario que representa una gráfica dirigida y regresa un 
    diccionario donde sus llaves son los nodos de la gráfica y los valores son
    el grado de entrada de ese nodo.

    Parámetros
    ----------
    d_grafica : TIPO. diccionario
        DESCRIPCIÓN. Gráfica dirigida, las claves representan los nodos y los 
        valores son conjunto de los nodos a los que se conectan.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no resive un diccionario como parámetro.

    Valor de retorno
    ----------------
    deg_in : TIPO. diccionario
        DESCRIPCIÓN. Las llaves de este diccionario son nodos y sus valores
        son entero que indican el grado de entrada de los nodos.

    """
    
    # validación del parámetro de entrada
    if type(d_grafica) is not dict:
        raise TypeError("el parámetro que recibe calcula_grados_de_entrada() tiene que ser un diccionario.")
        
    # valor de retorno es diccionario vacío
    deg_in = { }
    
    # contrucón de la tabla   
    for k in d_grafica.keys():
        k_deg = 0
        
        # verifica que nodos se enlazan al nodo que recorre actualmente
        for v in d_grafica.values():
            ady = list(v)
            k_deg += ady.count(k)
            
        deg_in[k] = k_deg
        
    return deg_in
        

def dist_grados_de_entrada(d_grafica):
    """
    Recibe un diccionario que representa una gráfica dirigida y regresa un 
    diccionario donde sus llaves son los grados de salida de la gráfica y los 
    valores son la frecuencia de los grados de entrada.

    Parámetros
    ----------
    d_grafica : TIPO. diccionario
        DESCRIPCIÓN. Gráfica dirigida, las claves representan los nodos y los 
        valores son conjunto de los nodos a los que se conectan.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no resive un diccionario como parámetro.

    Valor de retorno
    ----------------
    distr : TIPO. diccionario
            DESCRIPCIÓN. Las llaves de este diccionario son grados de salida y 
            sus valores son entero que indican la frecuencia de los grados de 
            entrada.
    """
    # TODO: ¿es posible optimisar? 
    
    # validación del parámetro de entrada
    if type(d_grafica) is not dict:
        raise TypeError("el parámetro que recibe dist_grados_de_entrada() tiene que ser un diccionario.")

    # obtiene la lista de los grados de entrada
    deg_in = list(calcula_grados_de_entrada(d_grafica).values())
    
    # umbral de grados a buscar en la lista
    deg_max = max(deg_in)
    
    # el valor de retorno es un diccionario vacío donde se gurdaran los datos
    distr = { }
    
    # recorre la lista para crear una tabla de distribución
    for i in range(deg_max + 1):
        
        # cuenta cuantos veces se encuentra el grado actual en la lista
        deg_count = deg_in.count(i)
        
        # TODO ¿Es necesario omitir los que son cero?
        # se resuelve agregando:
        # if deg_count != 0:
        distr[i] = deg_count
    
    return distr

    
def dist_normalizada_entrada(d_grafica):
    """
    Recibe un diccionario que representa una gráfica dirigida y regresa un 
    diccionario donde sus llaves son los grados de entrada de la gráfica y los 
    valores son la frecuencia normalizada de los grados de entrada.

    Parámetros
    ----------
    d_grafica : TIPO. diccionario
        DESCRIPCIÓN. Gráfica dirigida, las claves representan los nodos y los 
        valores son conjunto de los nodos a los que se conectan.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no resive un diccionario como parámetro.

    Valor de retorno
    ----------------
    distr_norm : TIPO. diccionario
        DESCRIPCIÓN. Las llaves de este diccionario son grados de entrada y sus 
        valores son flotantes que indican la frecuencia normalizada de los 
        grados de entrada.
    """
    
    # validación del parámetro de entrada
    if type(d_grafica) is not dict:
        raise TypeError("el parámetro que recibe dist_normalizada_entrada() tiene que ser un diccionario.")

    # distribución de los grados de entrada
    dist_in = dist_grados_de_entrada(d_grafica)
    total = sum(list(dist_in.values()))
    
    # el valor de retorno es un diccionario vacío donde se gurdaran los datos
    distr_norm = { }
    
    # se recorre el diccionario de distribución para crear un diccionario con
    # la distrubución normalizada 
    for k, v in dist_in.items():
        deg_in_norm = v/total
        distr_norm[k] = deg_in_norm
    
    return distr_norm


def grafica_distr_entrada(distr):
    """
    Recibe un diccionario que contenga la distrubución de los grados de 
    entrada de un grafo. Renderiza una figura con la gráfica de la 
    distribución.

    Parámetros
    ----------
    distr : dicccionario
        DESCRIPCIÓN. El diccionario contiene como valores la distrubución de 
        los grados de entrada nodales(enteros) de un gráfica dirigida.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no resive un diccionario como parámetro.

    Returns
    -------
    None.
        Se muestra la figura, pero el valor de retorno es None.
    """
    
    # validación del parámetro de entrada
    if type(distr) is not dict:
        raise TypeError("el parámetro que recibe grafica_distr_entrada() tiene que ser un diccionario.")
    
    valores_x = list(distr.keys())
    valores_y = list(distr.values())
    
    plt.plot(valores_x, valores_y, marker='o')
    plt.xlabel("Grado nodal")
    plt.ylabel("Número de nodos")
    plt.title("Distribución de grados de entrada")
    # plt.show()
    
    return


def grafica_distr_norm_entrada(distr_norm):
    """
    Recibe un diccionario que contenga la distrubución normalizada de los 
    grados de entrada de un grafo Renderiza una figura con la gráfica de la
    distribución normalizada.

    Parámetros
    ----------
    distr : dicccionario
        DESCRIPCIÓN. El diccionario contiene como valores la distrubución 
        normalizada de los grados de entrada nodales(flotantes) de un gráfica 
        dirigida.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no resive un diccionario como parámetro.

    Returns
    -------
    None.
        Se muestra la figura, pero el valor de retorno es None.
    """
    
    # validación del parámetro de entrada
    if type(distr_norm) is not dict:
        raise TypeError("el parámetro que recibe grafica_distr_norm_entrada() tiene que ser un diccionario.")
        
    valores_x = list(distr_norm.keys())
    valores_y = list(distr_norm.values())
    
    plt.plot(valores_x, valores_y, marker='o')
    plt.xlabel("Grado nodal")
    plt.ylabel("Número de nodos")
    plt.title("Distribución Normalizada de grados de entrada")
    # plt.show()

    return


## Extras práctica 1 ##########################################################

def calcula_grados_de_salida(d_grafica):
    """
    Recibe un diccionario que representa una gráfica dirigida y regresa un 
    diccionario donde sus llaves son los nodos de la gráfica y los valores son
    el grado de salida de ese nodo.

    Parámetros
    ----------
    d_grafica : TIPO. diccionario
        DESCRIPCIÓN. Gráfica dirigida, las claves representan los nodos y los 
        valores son conjunto de los nodos a los que se conectan.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no resive un diccionario como parámetro.

    Valor de retorno
    ----------------
    deg_out : TIPO. diccionario
        DESCRIPCIÓN. Las llaves de este diccionario son nodos y sus valores
        son entero que indican el grado de salida de los nodos.

    """
    
    # validación del parámetro de entrada
    if type(d_grafica) is not dict:
        raise TypeError("el parámetro que recibe calcula_grados_de_salida() tiene que ser un diccionario.")
        
    # el valor de retorno es un diccionario vacío donde se gurdaran los datos
    deg_out = { }
        
    # contrucón de la tabla   
    for k, v in d_grafica.items():
        
        # verificacada a cuantos nodos se enlaza al nodo que recorre actualmente
        deg_out[k] = len(v)
        
    return deg_out

def dist_grados_de_salida(d_grafica):
    """
    Recibe un diccionario que representa una gráfica dirigida y regresa un 
    diccionario donde sus llaves son los grados de salida de la gráfica y los 
    valores son la frecuencia de los grados de salida.

    Parámetros
    ----------
    d_grafica : TIPO. diccionario
        DESCRIPCIÓN. Gráfica dirigida, las claves representan los nodos y los 
        valores son conjunto de los nodos a los que se conectan.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no resive un diccionario como parámetro.

    Valor de retorno
    ----------------
    distr : TIPO. diccionario
        DESCRIPCIÓN. Las llaves de este diccionario son grados de salida y sus 
        val ores son entero que indican la frecuencia de los grados de salida.
        
    """
    # TODO: ¿es posible optimisar? 
    
    # validación del parámetro de entrada
    if type(d_grafica) is not dict:
        raise TypeError("el parámetro que recibe dist_grados_de_salida() tiene que ser un diccionario.")

    # obtiene la lista de los grados de entrada
    deg_out = list(calcula_grados_de_salida(d_grafica).values())
    
    # umbral de grados a buscar en la lista
    deg_max = max(deg_out) 
    
    # el valor de retorno es un diccionario vacío donde se gurdaran los datos
    distr = { }
    
    # recorre la lista para crear una tabla de distribución
    for i in range(deg_max + 1):
        
        # cuenta cuantos veces se encuentra el grado actual en la lista
        deg_count = deg_out.count(i)
        
        # TODO ¿Es necesario omitir los que son cero?
        # se resuelve agregando:
        # if deg_count != 0:
        distr[i] = deg_count
    
    return distr 


def dist_normalizada_salida(d_grafica):
    """
    Recibe un diccionario que representa una gráfica dirigida y regresa un 
    diccionario donde sus llaves son los grados de salida de la gráfica y los 
    valores son la frecuencia normalizada de los grados de salida.

    Parámetros
    ----------
    d_grafica : TIPO. diccionario
        DESCRIPCIÓN. Gráfica dirigida, las claves representan los nodos y los 
        valores son conjunto de los nodos a los que se conectan.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no resive un diccionario como parámetro.

    Valor de retorno
    ----------------
    distr_norm : TIPO. diccionario
        DESCRIPCIÓN. Las llaves de este diccionario son grados de salida y sus 
        valores son flotantes que indican la frecuencia normalizada de los 
        grados de salida.
    """
    
    # validación del parámetro de entrada
    if type(d_grafica) is not dict:
        raise TypeError("el parámetro que recibe dist_normalizada_salida() tiene que ser un diccionario.")

    # distribución de los grados de salida
    dist_out = dist_grados_de_salida(d_grafica)
    total = sum(list(dist_out.values()))
    
    # el valor de retorno es un diccionario vacío donde se gurdaran los datos
    distr_norm = { }
    
    # se recorre el diccionario de distribución para crear un diccionario con
    # la distrubución normalizada 
    for k, v in dist_out.items():
        deg_out_norm = v/total
        distr_norm[k] = deg_out_norm
    
    return distr_norm


def grafica_distr_salida(distr):
    """
    Recibe un diccionario que contenga la distrubución de los grados de salida 
    de un grafo. Renderiza una figura con la gráfica de la distribución.

    Parámetros
    ----------
    distr : dicccionario
        DESCRIPCIÓN. El diccionario contiene como valores la distrubución de 
        los grados de salida nodales(enteros) de un gráfica dirigida.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no resive un diccionario como parámetro.

    Returns
    -------
    None.
        Se muestra la figura, pero el valor de retorno es None.
    """
    
    # validación del parámetro de entrada
    if type(distr) is not dict:
        raise TypeError("el parámetro que recibe grafica_distr_salida() tiene que ser un diccionario.")
    
    valores_x = list(distr.keys())
    valores_y = list(distr.values())
    
    plt.plot(valores_x, valores_y, marker='o')
    plt.xlabel("Grado nodal")
    plt.ylabel("Número de nodos")
    plt.title("Distribución de grados de salida")
    # plt.show()
    
    return

def grafica_distr_norm_salida(distr_norm):
    """
    Recibe un diccionario que contenga la distrubución normalizada de los 
    grados de salida de un grafo Renderiza una figura con la gráfica de la
    distribución normalizada.

    Parámetros
    ----------
    distr : dicccionario
        DESCRIPCIÓN. El diccionario contiene como valores la distrubución 
        normalizada de los grados de salida nodales(flotantes) de un gráfica 
        dirigida.

    Excepción
    ---------
    TypeError
        DESCRIPCIÓN. Cuando no recibe un diccionario como parámetro.

    Valor de retorno
    ----------------
    None.
        Se muestra la figura, pero el valor de retorno es None.
    """
    
    # validación del parámetro de entrada
    if type(distr_norm) is not dict:
        raise TypeError("el parámetro que recibe grafica_distr_norm_salida() tiene que ser un diccionario.")
        
    valores_x = list(distr_norm.keys())
    valores_y = list(distr_norm.values())
    
    plt.plot(valores_x, valores_y, marker='o')
    plt.xlabel("Grado nodal")
    plt.ylabel("Número de nodos")
    plt.title("Distribución Normalizada de grados de salida")
    # plt.show()
    
    return


## Extras tarea 2 #############################################################

def aristas(red):
    """
    Recibe un diccionario que representa una gráfica y regresa el número de 
    aristas que tiene.

    Parámetros
    ----------
    red : diccionario
        Las llaves del diccionario son representan los nodos de la red y sus 
        valores son conjuntos que representan conecciones.

    Excepción
    ---------
    TypeError
        Se lanza cuando no se recibe un diccionario como parametro.

    Valor de retorno
    ----------------
    m : entero
        Es el número de arista de la red que entro como parámetro.
        
    """
    
    # validación de parametros de entrada
    if type(red) is not dict:
        raise TypeError("el parámetro que recibe densidad() tiene que ser un diccionario.")
       
    # se calcula los grados de entrada de los nodos de la red
    deg_in = calcula_grados_de_entrada(red)
    
    # se ocupa el agloritmo para saber las arista o enlaces de la red
    m = int( sum(list(deg_in.values())) / 2 )
    return m


def aristas_grafo_completo(n):
    """
    Resibe un número entero que es el número de nodos de un grafo del tipo K_n.

    Parámetros
    ----------
    n : entero
        El número de nodos en una gráfica completa.

    Excepciones
    -----------
    TypeError
        Se lanza cuando la función no recibe un entero
    ValueError
        Se lanza cuando el entero que recive es menor a 1

    Valor de retorno
    ----------------
    m : entero
        Es el número de arista de la de la gráfica completa.

    """

    # validación del parámetro de entrada
    if type(n) is not int:
        raise TypeError("el parámetro que recibe crea_un_grafo_completo() tiene que ser un entero positivo.")
    if n < 1:
        raise ValueError("el parámetro que recibe crea_un_grafo_completo() tiene que ser mayor a cero.")
    
    # se ocupa el algoritmo
    m = int(n * (n - 1) / 2)
    
    return m
    

## tarea 2 ####################################################################

def densidad(red):
    """
    Recibe una red y regresa la densidad de ésta.

    Parámetros
    ----------
    red : diccionario
        Las llaves del diccionario son representan los nodos de la red y sus 
        valores son conjuntos que representan conecciones.

    Excepciones
    -----------
    TypeError
        Se lanza cuando no recibe un diccionario como parámetro.

    Valor de retorno
    ----------------
    d : flotante
        la densidad de la red.

    """
    
    # validación de parametros de entrada
    if type(red) is not dict:
        raise TypeError("el parámetro que recibe densidad() tiene que ser un diccionario.")

    # con el número de nodos se puden obtener información de las aristas del 
    # gráfo y de su grágo completo
    v = numero_nodos(red)
    
    m_g = aristas(red)
    m_kn = aristas_grafo_completo(v)
    
    d = m_g / m_kn  # se calcula la densidad 
    
    return d


def grafica_aleatoria(n, p):
    """
    Genera una gráfica aleatorea.

    Parámetros
    ----------
    n : entero
        El número de nodos de la gráfica. Tiene que ser un entero positivo 
        mayor a cero.
    p : flotante
        la probabilidad de que los nodos se conecten. Tinene que ser tener que
        ser mayor o igual a cero y ser menor o igual a 1.

    Excepciones
    -----------
    TypeError
        Se lanza cuando 'n' no es un entero, o 'p' no es un flotante.
    ValueError
        Se lanza cuando 'n' no es mayor a cero, o cuando 'p' no cumple la
        condición 0 <= p <= 1.

    Valor de retorno
    ----------------
    g : diccionario
        El diccionario representa una gráfica, sus llaves representan los nodos
        y los valores sus valores son conjuntos que representan conecciones.

    """
    
    # validación de los parámetros de entrada
    
    # validación de n
    if type(n) is not int:
        raise TypeError("el parámetro 'n' recibe grafica_aleatoria() tiene que ser un entero positivo.")
    if n < 1:
        raise ValueError("el parámetro 'n' recibe grafica_aleatoria() tiene que ser mayor a cero.")
        
    # validación de p
    if type(p) is not float:
        raise TypeError("el parámetro 'p' recibe grafica_aleatoria() tiene que ser un flotante positivo.")
    if not 0 <= p <= 1:
        raise ValueError("el parámetro 'p' recibe grafica_aleatoria() tiene que valer entre 0.0 y 1.0.")
    
    # TODO mejorar el algoritmo. no me gusta la cantidad de 'for'
    
    # la gráfica vacía, cada nodo tiene una lista de adyacencia vacia
    g = { }
    for i in range(n):
        g[i] = set()
        
    # cola con los nodos. es una lista común pero se usara como cola
    cola = [ ]
    for i in range(n):
        cola.append(i)
    # sacamos el primer elemento, no es útil
    cola.pop(0)
    
    # El bucle hace les conecciones de la gráfica aleatoriamente, n-1 es por 
    # que las conecciones se habrán hecho todas al tomar el penultimo nodo
    for i in range(n-1):

        for j in cola:
            
            a = random.random()
            if a < p:
                g[i].add(j)
                g[j].add(i)
                    
        # sacamos el primer elemtno de la cola, ya se han hecho sus conecciones
        cola.pop(0)
        
    return g

###############################################################################
## zona de tarea/práctica actual
###############################################################################

print("***Gráficas aleatorias con n=10 y p=0.3***",end='\n\n')
n = 10
p = 0.3
for i in range(5):
    
    graf_al = grafica_aleatoria(n, p)
    print("Gráfica", i + 1,":")
    print(graf_al)
    print("Su densidad es:", end=" ")
    print(densidad(graf_al), end='\n\n')

print("***Gráficas aleatorias con n=10 y p=0.6***",end='\n\n')
n = 10
p = 0.6
for i in range(5):
    
    graf_al = grafica_aleatoria(n, p)
    print("Gráfica", i + 1,":")
    print(graf_al)
    print("Su densidad es:", end=" ")
    print(densidad(graf_al), end='\n\n')

n = 5
p = 1.0
graf_comp = grafica_aleatoria(n, p)
print("Gráfica completa :")
print(graf_comp)
print("Su densidad es:", end=" ")
print(densidad(graf_comp), end='\n\n')



###############################################################################
## zona de pruebas
###############################################################################

if __name__ == "__main__":

    _amistades = {'Alicia':{'Beto','Carlos','Carmen','David','Mónica'},
                 'Beto':{'Alicia','Jorge'},
                 'Carlos':{'Alicia','David','Mónica'},
                 'Carmen':{'Alicia','Mónica'},
                 'David':{'Alicia','Carlos'},
                 'Enrique':{'Irene','Jorge','Rosa'},
                 'Jorge':{'Beto','Enrique','Irene','Rosa'},
                 'Irene':{'Enrique','Jorge','Rosa'},
                 'Mónica':{'Alicia','Carlos','Carmen'},
                 'Rosa':{'Enrique','Irene','Jorge'}}   
            
    _graf1 = {1: {2}, 2: {4}, 3: {2}, 4: {1, 3, 5}, 5: {2, 4, 6}, 6: {1}}
    
    
    ## pruebas tarea 1 --------------------------------------------------------
    print("Prueba de numero_nodos")
    print(numero_nodos(_amistades), end='\n\n')    
    
    print("Prueba de calcula_grados")
    print(calcula_grados(_amistades), end='\n\n')
    
    print("Prueba de grado_maximo")
    print(grado_maximo(_amistades), end='\n\n')
    
    ## pruebas práctica 1 -----------------------------------------------------
    print("Prueba de crea_un_grafo_completo")
    print(crea_un_grafo_completo(5), end='\n\n')
    
    print("Prueba de calcula_grados_de_entrada")
    print(calcula_grados_de_entrada(_graf1), end='\n\n')
    
    print("Prueba de dist_grados_de_entrada")
    print(dist_grados_de_entrada(_graf1), end='\n\n')
    
    print("Prueba de dist_normalizada_entrada")
    print(dist_normalizada_entrada(_graf1), end='\n\n')
    
    print("Prueba de grafica_distr_entrada")
    #print(grafica_distr_entrada(dist_grados_de_entrada(_graf1)), end='\n\n')
    
    print("Prueba de grafica_distr_entrada")
    #print(grafica_distr_norm_entrada(dist_normalizada_entrada(_graf1)), end='')
    print("")
    
    ## pruebas práctica 1  extras ---------------------------------------------
    print("Prueba de calcula_grados_de_salida")
    print(calcula_grados_de_salida(_graf1), end='\n\n')
    
    print("Prueba de dist_grados_de_salida")
    print(dist_grados_de_salida(_graf1), end='\n\n')
    
    print("Prueba de dist_normalizada_salida")
    print(dist_normalizada_salida(_graf1), end='\n\n')
    
    print("Prueba de grafica_distr_salida")
    #print(grafica_distr_salida(dist_grados_de_salida(_graf1)), end='\n\n')
    
    print("Prueba de grafica_distr_entrada")
    #print(grafica_distr_norm_salida(dist_normalizada_salida(_graf1)), end='')
    print("")
    
    ## pruebas tarea 2 extras ------------------------------------------------
    
    print("Prueba de aristas")
    print(aristas(_amistades), end='\n\n')
    
    print("Prueba de aristas_grafo_completo")
    print(aristas_grafo_completo(5), end='\n\n')

    ## pruebas tarea ----------------------------------------------------------
    print("Prueba de densidad")
    print(densidad(_amistades), end='\n\n')
    
    print("Prueba de grafica_aleatoria")
    print(grafica_aleatoria(10, 0.02), end='\n\n')