import csv
from math import *
import folium
from collections import namedtuple

Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, ubicacion')
Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')

def lee_estaciones(fichero):
    ''' Lee el fichero de datos y devuelve una lista de estaciones
    
    ENTRADA: 
       :param fichero: Nombre y ruta del fichero a leer
       :type fichero: str
   
    SALIDA: 
       :return: Lista de tuplas de tipo Estacion
       :rtype: [Estacion(str, int, int, int, Coordenadas(float, float))]
    
    Cada estación se representa con una tupla con los siguientes valores:
    - Nombre de la estación
    - Número total de bornetas
    - Número de bornetas vacías
    - Número de bicicletas disponibles
    - Ubicacion
    Usaremos el módulo csv de la librería estándar de Python para leer el
    fichero de entrada.
    Hay que saltar la línea de encabezado del fichero y comenzar a leer los datos
    a partir de la segunda línea.
    Hay que realizar un pequeño procesamiento con los datos numéricos. Hay que
    pasar del formato cadena (que es lo que se interpreta al leer el csv) a un
    valor numérico (para poder aplicar operaciones matemáticas si fuese necesario).
    También hay que crear una tupla con nombre de tipo Coordenadas
    '''
    with open(fichero,encoding='utf-8') as f:
      lista = []
      lector = csv.reader(f)
      next(lector)
      for nombre, bornetas, bornetas_vacias, bicis_disponibles, latitud, longitud in lector:
         bornetas = int(bornetas)
         bornetas_vacias = int(bornetas_vacias)
         bicis_disponibles = int(bicis_disponibles)
         latitud = float(latitud)
         longitud = float(longitud)
         ubicacion = Coordenadas(latitud,longitud)
         tupla = Estacion(nombre,bornetas,bornetas_vacias,bicis_disponibles,ubicacion)
         lista.append(tupla)
    return lista

def estaciones_bicis_libres(estaciones, k=5):
    ''' Estaciones que tienen bicicletas libres
    
    ENTRADA: 
      :param estaciones: lista de estaciones disponibles 
      :type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
      :param k: número mínimo requerido de bicicletas
      :type k: int
    SALIDA: 
      :return: lista de estaciones seleccionadas
      :rtype: [(int, str)] 
    
    Toma como entrada una lista de estaciones y un número k.
    Crea una lista formada por tuplas (número de bicicletas libres, nombre)
    de las estaciones que tienen al menos k bicicletas libres. La lista
    estará ordenada de mayor a menor por el número de bicicletas libres.
    '''
    lista = []
    for estacion in estaciones:
       if estacion.bicis_disponibles >= k :
          tupla = (estacion.bicis_disponibles,estacion.nombre,estacion.ubicacion)
          lista.append(tupla)
          lista.sort()
          lista.reverse()
    return lista

def calcula_distancia(coordenadas1, coordenadas2):
    ''' Distancia entre un punto y una estación
    ENTRADA: 
    :param coordenadas1: coordenadas del primer punto
    :type coordenadas1: Coordenadas(float, float)
    :param coordenadas2: coordenadas del segundo punto
    :type coordenadas2: Coordenadas(float, float)
      
    SALIDA: 
    :return: distancia entre dos coordenadas
    :rtype: float 
    
    Toma como entrada dos coordenadas y calcula la distancia entre ambas aplicando la fórmula
    
        distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
    '''
    x2, x1 = coordenadas1[1],coordenadas1[0]
    y2, y1 = coordenadas2[1],coordenadas2[0]
    distancia = sqrt((x2-x1)**2 + (y2-y1)**2)
    return distancia

def estaciones_cercanas(estaciones, coordenadas, k=5):
    ''' Estaciones cercanas a un punto dado
    
    ENTRADA: 
      :param estaciones: lista de estaciones disponibles
      :type estaciones: [Estacion(str, int, int, int, Coordenadas(float, float))]
      :param coordenadas: coordenadas formada por la latitud y la longitud de un punto
      :type coordenadas: Coordenadas(float, float)
      :param k: número de estaciones cercanas a calcular 
      :type k: int
    SALIDA: 
      :return: Una lista de tuplas con la distancia, nombre y bicicletas libres de las estaciones seleccionadas 
      :rtype: [(float, str, int)] 
    
    Toma como entrada una lista de estaciones,  las coordenadas de  un punto y
    un valor k.
    Crea una lista formada por tuplas (distancia, nombre de estación, bicicletas libres)
    con las k estaciones con bicicletas libres más cercanas al punto dado, ordenadas por
    su distancia a las coordenadas dadas como parámetro.
    '''
    esbici = estaciones_bicis_libres(estaciones,1)
    distancias = []
    res_distancias = []
    for estacion in esbici:
       distancia = calcula_distancia(coordenadas,estacion[2])
       tupla = (distancia,estacion[1],estacion[0])
       distancias.append(tupla)
    distancias.sort()
    for i in range(0,k+1):
       res_distancias.append(distancias[i])
    return res_distancias

    