from os import system
system("cls")
import re
import json

#Se crean constantes para facilitar el manejo del json y evitar errores de tipeo
#SECCION CONSTANTES

EQUIPO = "equipo"
JUGADORES = "jugadores"
NOMBRE = 'nombre'
POSICION = 'posicion'
LOGROS = 'logros'
ESTADISTICAS = "estadisticas"
ESTADISTICA_TEMPORADA = "temporadas"
ESTADISTICA_PUNTOS_TOTALES = "puntos_totales"
ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO = "promedio_puntos_por_partido"
ESTADISTICA_REBOTES_TOTALES = "rebotes_totales"
ESTADISTICA_PROMEDIO_REBOTES_POR_PARTIDO = "promedio_rebotes_por_partido"
ESTADISTICA_ASISTENCIAS_TOTALES = "asistencias_totales"
ESTADISTICA_PROMEDIO_ASISTENCIAS_POR_PARTIDO = "promedio_asistencias_por_partido"
ESTADISTICA_ROBOS_TOTALES = "robos_totales"
ESTADISTICA_BLOQUEOS_TOTALES = "bloqueos_totales"
ESTADISTICA_PORCENTAJE_TIROS_DE_CAMPO = "porcentaje_tiros_de_campo"
ESTADISTICA_PORCENTAJE_TIROS_LIBRES =  "porcentaje_tiros_libres"
ESTADISTICA_PORCENTAJE_TIROS_TRIPLES =  "porcentaje_tiros_triples"

PUNTOS_CSV = 'puntos'
REBOTES_CSV = 'rebotes'
ASISTENCIAS_CSV = 'asistencias'
ROBOS_CSV = 'robos'

#FIN SECCION CONSTANTES






#INICIO FUNCIONES *******

def leer_archivo()->list:
    """
      lee un archivo JSON y devuelve una lista de jugadores.
     :return: lista de jugadores del archivo "dt_dream_teams.json".
    """
   
    with open("parcial_dream\datos\dt_dream_teams.json", 'r') as archivo:
        diccionario = json.load(archivo)
    return diccionario[JUGADORES]

#lista_jugadores Se utiliza para leer el archivo json y acceder a los mismos
lista_jugadores = leer_archivo()

def print_space():
    print("----------------")
    print("----------------")    
    print("----------------")
    
def es_numero(caracter:str) -> bool:
    """
    :caracter: str recibe un texto por parametro
    Obtiene si un caracter es numero o nó
    :return: bool
    """
    if caracter.isdigit():
        return True
    else:
        return False

def muestra_jugador_por_posicion(listado:list):
    """
     Esta función toma una lista de jugadores e imprime su nombre y posición.    
    :param listado: El parametro es un lista que representa a los jugadores    
    """
    for jugador in listado:
        print("Nombre {0} - Posición: {1}".format(jugador[NOMBRE], jugador[POSICION]))

def muestra_jugadores_con_indice(listado:list):
     """
     Esta función toma una lista de jugadores e imprime su nombre, posición, contador (mas un indice correspondiente a su ubicacion dentro de la lista)
     :param listado: El parametro es un lista que representa a los jugadores
     """
     contador = -1
     for jugador in listado:
         contador += 1
         print("{1}: {0}".format(jugador[NOMBRE] , (contador)))

def mostrar_estadisticas_jugador(jugador):
    """
    Recibe un jugador e imprime sus estadisticas
    param jugador: El parametro es un lista que representa a los jugadores
    """
    print("**Estadistica de {0} ****".format(jugador[NOMBRE]))
    print("TEMPORADA = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_TEMPORADA]))
    print("PUNTOS TOTALES = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_PUNTOS_TOTALES]))
    print("PROMEDIO PUNTOS POR PARTIDO = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO]))
    print("REBOTES TOTALES = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_REBOTES_TOTALES]))
    print("PROMEDIO REBOTES_POR_PARTIDO = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_PROMEDIO_REBOTES_POR_PARTIDO]))
    print("ASISTENCIAS TOTALES = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_ASISTENCIAS_TOTALES]))
    print("PROMEDIO ASISTENCIAS POR PARTIDO = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_PROMEDIO_ASISTENCIAS_POR_PARTIDO]))
    print("ROBOS TOTALES = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_ROBOS_TOTALES]))
    print("BLOQUEOS TOTALES = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_BLOQUEOS_TOTALES]))
    print("PORCENTAJE TIROS DE CAMPO = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_PORCENTAJE_TIROS_DE_CAMPO]))
    print("PORCENTAJE TIROS LIBRES = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_PORCENTAJE_TIROS_LIBRES]))
    print("PORCENTAJE TIROS TRIPLES = {0}".format(jugador[ESTADISTICAS][ESTADISTICA_PORCENTAJE_TIROS_TRIPLES]))

def mostrar_estadisticas_jugador_por_indice():
    """
    Muestra las estadisticas de un jugador seleccionado por indice
    Opcionalmente exporte el resultado a un csv
    """
    entrada = ""
    indice = 0
    indice_es_valido_flag: bool = False
    jugador_seleccionado = None
    
    while not es_numero(entrada) or not indice_es_valido_flag:

        entrada = input("Selecciona un jugador por su índice: ")
        if (entrada.isdigit()):
            indice = int(entrada)
            if indice >= 0 and indice < len(lista_jugadores):
                indice_es_valido_flag = True
                jugador_seleccionado = lista_jugadores[indice]
                mostrar_estadisticas_jugador(jugador_seleccionado)
                confirmacion = input("Por favor, ingresa 'S' para crear csv: ")
                if  confirmacion.upper() == 'S':
                    print("Generando CSV...............")
                    pathCsv:str = "parcial_dream\\csv\\" + jugador_seleccionado[NOMBRE]
                    generar_csv(pathCsv + ".csv", jugador_seleccionado)
                    print("CSV Generado punto 3 en la carpeta " + pathCsv + jugador_seleccionado[NOMBRE] + ".csv" )
                else:
                    print("Indice ingresado no válido")
                
def generar_csv(nombre_archivo:str, jugador):
    """
    Genera un CSV de las estadisticas por jugador 
    parametro: nombre_archivo: con formato "nombre_archivo.csv" y 
    parametro: jugador:  representa a la informacion de un jugador
    """
    with open(nombre_archivo, "w") as archivo_csv:
        texto_linea = "NOMBRE,TEMPORADA,PUNTOS_TOTALES,PROMEDIO_PUNTOS_POR_PARTIDO,REBOTES_TOTALES,PROMEDIO_REBOTES_POR_PARTIDO,ASISTENCIAS_TOTALES,PROMEDIO_ASISTENCIAS_POR_PARTIDO,ROBOS_TOTALES,BLOQUEOS_TOTALES,PORCENTAJE_TIROS_DE_CAMPO,PORCENTAJE_TIROS_LIBRES,PORCENTAJE_TIROS_TRIPLES"
        archivo_csv.write(texto_linea)
        texto_linea ="\n";
        texto_linea += jugador[NOMBRE]
        texto_linea += ", " + str(jugador[ESTADISTICAS][ESTADISTICA_TEMPORADA])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_PUNTOS_TOTALES])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_REBOTES_TOTALES])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_PROMEDIO_REBOTES_POR_PARTIDO])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_ASISTENCIAS_TOTALES])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_PROMEDIO_ASISTENCIAS_POR_PARTIDO])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_ROBOS_TOTALES])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_BLOQUEOS_TOTALES])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_PORCENTAJE_TIROS_DE_CAMPO])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_PORCENTAJE_TIROS_LIBRES])
        texto_linea += "," +  str(jugador[ESTADISTICAS][ESTADISTICA_PORCENTAJE_TIROS_TRIPLES])

        archivo_csv.write(texto_linea)               

def mostrar_logros_de_un_jugador(parametro_nombre:str):
    """
    Muestra los logros de los jugadores que coinciden con el parametro_nombre
    parametro: parametro_nombre: texto a buscar 
    """
    parametro_nombre = parametro_nombre.lower()
    resultados = []
    patron = re.compile(r'\b' + re.escape(parametro_nombre) + r'\b', re.IGNORECASE)

    for jugador in lista_jugadores:
        if re.match(patron, jugador[NOMBRE]):
            resultados.append(jugador)

    if resultados:
        for jugador in resultados:
            print(f"Jugador: {jugador[NOMBRE]}")
            print(f"Posición: {jugador[POSICION]}")
            print("Logros:")
            for logro in jugador[LOGROS]:
                print(f"- {logro}")            
    else:
        print("No se encontró ningún jugador con ese nombre.")

def buscar_por_nombre():
    """
    Esta función solicita al usuario que ingrese el nombre de un jugador y luego llama a otra función para mostrar los logros de ese jugador.
    """
    nombre_jugador = str(input("Ingrese nombre del jugador: "))
    mostrar_logros_de_un_jugador(nombre_jugador)   

def calcular_promedio_estadistica(listado: list, campo: str):
    """
    Esta función calcula el promedio de un campo específico en una lista de diccionarios.    
     :param listado: una lista de diccionarios que contienen datos estadísticos     
     :param campo: El parámetro "campo" es una cadena de cual calcularemos el promedio     
     :return: el valor promedio de un campo específico. Si la lista es vacío, la función devuelve 0.
    """
    if len(listado) == 0:
        return 0
    total = 0
    for item in listado:
        total += item[ESTADISTICAS][campo]

    promedio = total / len(listado)
    return promedio

def ordenar_listado_por_estadistica(listado:list, campo: str, orden: str) -> list:
    """
    Esta función ordena una lista de diccionarios por un campo específico en orden ascendente (asc) o descendente (desc).    
    :param listado: :param listado: una lista de diccionarios, donde cada diccionario representa un ítem con su
     estadísticas correspondientes    
    :param campo: cadena que representa el campo por el cual se debe ordenar la lista (por ejemplo, "puntos_totales")     
    :param orden: asc ó desc ( solo acepta estos valores)
    :return: una lista ordenada
    """
    listado_ordenado = []
    if orden == 'asc':
        listado_ordenado = sorted(listado, key=lambda x: x[ESTADISTICAS][campo])
    elif orden == 'desc':
        listado_ordenado = sorted(listado, key=lambda x: x[ESTADISTICAS][campo], reverse=True)
    else:
        print("Orden no válido.")
        exit()
    return listado_ordenado

def calcular_max(listado:list, key:str):    
    """
    La función calcula el valor máximo de una clave específica en una lista.    

    :param listado: una lista de diccionarios, donde cada diccionario representa un ítem con varios atributos
    :param key: El parámetro "key" es una cadena que representa un atributo del diccionario    
    :return: el elemento de la lista de entrada que tiene el valor más alto para la clave especificada.
    """
    flag_primer_item = True
    item_maximo = None
    for item in listado:    
        if flag_primer_item == True or item[key] > item_maximo[key]:
            flag_primer_item = False            
            item_maximo = item        
    return item_maximo

def buscar_jugador_mayor_por_campo(listado, campo):
    """
    Esta función toma una lista de jugadores y un campo, crea una nueva lista con el nombre del jugador y
     su valor máximo para ese campo, calcula el jugador con el valor máximo más alto e imprime
     su nombre y registro para ese campo.
    
    :param listado: una lista de diccionarios que contienen información sobre los jugadores y sus estadísticas
    :param campo: una cadena que representa el campo o estadística que queremos encontrar el valor máximo entre una lista de jugadores
    """

    nueva_lista = []
    for item in listado:
        nueva_lista.append({NOMBRE: item[NOMBRE], 'maximo': item[ESTADISTICAS][campo]})
    resultado = calcular_max(nueva_lista, 'maximo')
    print(campo + " = " + resultado[NOMBRE] + " - Record = " + str(resultado["maximo"]))
    
def promedio_arriba_de_un_valor(listado: list, valor_ingresado:int, campo:str):
    """
    La función imprime el nombre y el valor de un campo específico para los elementos de una lista que tienen un valor
     mayor que un valor de entrada dado.
    
    :param listado: lista de jugadores    
    :param valor_ingresado: El valor que se utilizará como valor maximo para filtrar la lista. Solo
     los elementos con un valor superior a este se imprimirán    
    :param campo: El parámetro "campo" es una cadena que representa el nombre de un atributo en
     un diccionario que se almacena dentro de cada elemento de la lista de entrada "listado"
    """
    for item in listado:
        if item[ESTADISTICAS][campo] > valor_ingresado:
            print(NOMBRE + ": " + item[NOMBRE] + " " + campo + ": " + str(item[ESTADISTICAS][campo]))

def buscar_jugador_con_mas_logros(listado):        
    """
    busca e imprime el jugador con mas logros
    :param listado:  listada de jugadores
    """
    jugador = None
    flag_primera_vez = True
    for item in listado:        
        if flag_primera_vez or len(item[LOGROS]) > len(jugador[LOGROS]):
            flag_primera_vez = False
            jugador = item    
    
    print("Jugador con mas logros " + jugador[NOMBRE] + " - Record = " + str(len(jugador[LOGROS])))

def mostrar_logros_de_un_jugador(parametro_nombre):
    """
    busca e imprime el jugador con mas logros segun el parametro_nombre ingresado
    :param parametro_nombre:  listada de jugadores
    """
    resultados = []
    patron = rf"{parametro_nombre}" 
    for jugador in lista_jugadores:
        if re.search(patron, jugador[NOMBRE].lower()):
            resultados.append(jugador)

    if resultados:
        for jugador in resultados:
            print(f"Jugador: {jugador[NOMBRE]}")
            print(f"Posición: {jugador[POSICION]}")
            print("Logros:")
            for logro in jugador[LOGROS]:
                print(f"- {logro}")            
    else:
        print("No se encontró ningún jugador con ese nombre.")            
                
def es_miembro_salon_fama(logros) -> str:
    """
    Indica si es o no miembro del salon de la fama
    :param logros:  lista de logros de un jugador
    :return: Sí o No
    """
    buscar = "fama"
    patron = rf"{buscar}"  
    es_miembro = False
    for item in logros:
        if re.search(patron, item.lower()):
            es_miembro = True
            break
    if es_miembro:
        return "Sí"
    else:
        return "No"

          
def mostrar_jugador_y_salon_fama(parametro_nombre):
    """
    Muestra e imprime si es/son o no miembro del salon de la fama segun el pparametro_nombre
    :param parametro_nombre:  texto a buscar contra los nombre de los jugadores
    """
    resultados = []    
    patron = rf"{parametro_nombre}"    
    for jugador in lista_jugadores:        
        if re.search(patron, jugador[NOMBRE].lower()):
            resultados.append(jugador)

    if resultados:
        for jugador in resultados:
            print(f"Nombre: {jugador[NOMBRE]}")
            print(f"Miembro Salon de la fama: {es_miembro_salon_fama(jugador[LOGROS])}")
            print("-------------------")
    else:
        print("No se encontró ningún jugador con ese nombre.")

def ordenar_listado_por_campo(listado:list, campo: str, orden: str) -> list:
    """
    Ordena el listado segun parametros, campo, y orden (asc o desc)
    :param listado: Listado
    :param campo: por el cual se ordenara la lista
    :param orden: asc= ascendente, desc= descendente 
    :return lista ordenada segun parametros
    """
    listado_ordenado = []    
    if orden == 'asc':
        listado_ordenado = sorted(listado, key=lambda x: (x.get(campo, 0), x.get("valor", 0)))
    elif orden == 'desc':
        listado_ordenado = sorted(listado, key=lambda x: (x.get(campo, 0), x.get("valor", 0)), reverse=True)
    else:
        print("Orden no válido.")
        exit()
    return listado_ordenado

def obtener_promedio_arriba_de_un_valor(listado: list, valor_ingresado:int, campo:str):
    """
    Obtiene los jugadores en donde la estadistica segun el parametro "campo" es mayor al parametro "valor_ingresado"
    :param listado: Listado con formato {nombre, posicion, "campo"}
    :param Valor Ingresado: valor maximo a contar
    :param campo: Campo a filtrar dentro de las estadisticas    
    :return lista una nueva lista segun los criterios campo y valor ingresado
    """
    nueva_lista = []
    for item in listado:        
        if item[ESTADISTICAS][campo] > valor_ingresado:
            nueva_lista.append({NOMBRE: item[NOMBRE], 'posicion': item[POSICION], 'valor': item[ESTADISTICAS][campo] })
    return nueva_lista

def generar_bonus_csv(nombre_archivo:str, listado:list):
    """
    Genera un csv con el formato Jugador,Puntos,Rebotes,Asistencias,Robos
    y lo graba segun el parametro "nombre_archivo"  e imprime la informacion correspondiente
    :param nombre_archivo: Nombre del archivo, se espera pór ejemplo "resultado.csv"
    :param listado: una lista con el formato "Jugador,Puntos,Rebotes,Asistencias,Robos"
     Crea un CSV
    """
    print("Generando CSV Bonus...")
    with open(nombre_archivo, "w") as archivo_csv:
        texto_linea = "Jugador,Puntos,Rebotes,Asistencias,Robos"
        archivo_csv.write(texto_linea)
        for jugador in listado:            
            texto_linea ="\n"
            texto_linea += jugador[NOMBRE]
            texto_linea += ", " + str(jugador[PUNTOS_CSV])
            texto_linea += ", " + str(jugador[REBOTES_CSV])
            texto_linea += ", " + str(jugador[ASISTENCIAS_CSV])
            texto_linea += ", " + str(jugador[ASISTENCIAS_CSV])
            archivo_csv.write(texto_linea)
    print("Generado CSV Bonus en csv/bonus.csv")


def ordenar_ranking_por_criterio(listado:str):    
    """
     Esta función ordena una lista por diferentes criterios y asigna una clasificación a cada elemento
     basado en ella. Se recorre cada filtro y por cada filtro se ordena de forma desc o sea de mayor a menor, 
     y mediante un contador se asigna la posicion en el ranking
     :param listado: una lista que representan a los jugadores y sus estadísticas.
     Los diccionarios tienen claves para 'puntos', 'rebotes', 'asistencias' y 'robos' .      
     :return: una lista ordenada segun un ranking por criterio o filtro
    """
    filtros = ['puntos', 'rebotes', 'asistencias','robos']
    for filtro in filtros:
        listado = sorted(listado, key=lambda x: x.get(filtro, 0), reverse=True)
        contador = 1
        for item in listado:
            match(filtro):
                case 'puntos':
                    item[PUNTOS_CSV] = contador #str(contador) + " ("+ str(item['puntos']) +")"
                case 'rebotes':
                    item[REBOTES_CSV] = contador #str(contador) + " ("+ str(item['rebotes']) +")"
                case 'asistencias':
                    item[ASISTENCIAS_CSV] = contador #str(contador) + " ("+ str(item['asistencias']) +")"
                case 'robos':
                    item[ROBOS_CSV] = contador #str(contador) + " ("+ str(item['robos']) +")"                
            contador += 1
    return listado

def bonus(listado:list):
    """    
    crea una nueva lista en base a la recibida por parametro con el formato
    nombre, puntos, rebotes,asistencias, robos
    :param listado: lista de  jugadores    
    : return: una nueva lista ordenada
    """
    nueva_lista = []
    for item in listado:        
        nueva_lista.append({'nombre': item[NOMBRE],                             
                            'puntos': item[ESTADISTICAS][ESTADISTICA_PUNTOS_TOTALES], 
                            'rebotes': item[ESTADISTICAS][ESTADISTICA_REBOTES_TOTALES], 
                            'asistencias': item[ESTADISTICAS][ESTADISTICA_ASISTENCIAS_TOTALES], 
                            'robos': item[ESTADISTICAS][ESTADISTICA_ROBOS_TOTALES]
                            })
    lista_ordenada = ordenar_ranking_por_criterio(nueva_lista)
    lista_ordenada = sorted(lista_ordenada, key=lambda x: x.get(PUNTOS_CSV, 0))
    return lista_ordenada

#FIN FUNCIONES *******


while True:
    
    print("--------------")
    respuesta_str = input("1: Muestra jugador y su posicion : \n2 Muestra jugador con su indice y/o imprime csv (Punto 3)  : \n3 Muestra logros de jugadores por criterio nombre (regex) : \n4 Muestra de manera ascendente el promedio de puntos por partido: \n5 muestra si el/los jugadores es/son miembro/s del salon de la fama por criterio nombre (regex)\n6 jugador con mayor cantidad de rebotes: \n7 jugador con mayor porcentaje de tiro de campo: \n8 jugador con mayor cantidad de asistencias totales: \n9 Jugador que promedia mas puntos por partido: \n10 jugador que promedia mas rebotes por partido: \n11 jugador que promedia mayor asistencia por partido: \n12 jugador con mayor cantidad de robos totales: \n13 jugador con mayor cantidad de bloqueos totales: \n14 jugador porcentaje tiros libres superior al ingresado: \n15 muestra promedios por punto de partido, excluyendo al que menor promedio tiene \n16 jugador con mas logros: \n17 jugador con mayor porcentaje de tiros triples: \n18 jugador con mayor cantidad temporadas jugadas \n19 Muestra los jugadores con porcentaje tiros de campo superior a valor ingresado \n20 Bonus \n ****Elija una opcion*** \n")
    respuesta_int = int(respuesta_str)
    
    match(respuesta_int):
        case 1:
            muestra_jugador_por_posicion(lista_jugadores)
            print_space()
        case 2:
            muestra_jugadores_con_indice(lista_jugadores)
            mostrar_estadisticas_jugador_por_indice()
            print_space()  
        case 3:
            nombre_jugador = str(input("Ingrese nombre del jugador: "))
            mostrar_logros_de_un_jugador(nombre_jugador)
            print_space()       
        case 4:
            lista_ordenada = ordenar_listado_por_estadistica(lista_jugadores, ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO, "asc")
            for item in lista_ordenada:
                print(item[NOMBRE], "-", item[ESTADISTICAS][ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO])
            print("Promedio General: " + str(calcular_promedio_estadistica(lista_jugadores, ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO)))
            print_space() 
        case 5:
            nombre_jugador = str(input("Ingrese nombre del jugador: "))
            mostrar_jugador_y_salon_fama(nombre_jugador)
            print_space() 
        case 6:
            buscar_jugador_mayor_por_campo(lista_jugadores, ESTADISTICA_REBOTES_TOTALES)
            print_space() 
        case 7:
            buscar_jugador_mayor_por_campo(lista_jugadores, ESTADISTICA_PORCENTAJE_TIROS_DE_CAMPO)
            print_space() 
        case 8:
            buscar_jugador_mayor_por_campo(lista_jugadores, ESTADISTICA_ASISTENCIAS_TOTALES)
            print_space() 
        case 9:
            valor = int(input("Ingrese un valor numérico promedio puntos por partido"))
            promedio_arriba_de_un_valor(lista_jugadores, valor ,ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO)
            print_space()
        case 10:
            valor = int(input("Ingrese un valor numérico promedio rebotes por partido"))
            promedio_arriba_de_un_valor(lista_jugadores, valor ,ESTADISTICA_PROMEDIO_REBOTES_POR_PARTIDO)
            print_space()
        case 11:
            valor = int(input("Ingrese un valor numérico promedio asistencias por partido"))
            promedio_arriba_de_un_valor(lista_jugadores, valor ,ESTADISTICA_PROMEDIO_ASISTENCIAS_POR_PARTIDO)
            print_space()
        case 12:
            buscar_jugador_mayor_por_campo(lista_jugadores, ESTADISTICA_ROBOS_TOTALES)
            print_space()
        case 13:
            buscar_jugador_mayor_por_campo(lista_jugadores, ESTADISTICA_BLOQUEOS_TOTALES)
            print_space()
        case 14:
            valor = int(input("Ingrese un valor numérico - porcentaje de tiros libres"))
            promedio_arriba_de_un_valor(lista_jugadores, valor, ESTADISTICA_PORCENTAJE_TIROS_TRIPLES)
            print_space()
        case 15:
            lista_ordenada = ordenar_listado_por_estadistica(lista_jugadores, ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO, "asc")
            elemento_eliminado = lista_ordenada.pop(0)
            for item in lista_ordenada:
                print(item[NOMBRE], "-", item[ESTADISTICAS][ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO])
            print("**************" )
            print("el elemento eliminado es", elemento_eliminado[NOMBRE], "-", elemento_eliminado[ESTADISTICAS][ESTADISTICA_PROMEDIO_PUNTOS_POR_PARTIDO])
            print_space()
        case 16:  
            buscar_jugador_con_mas_logros(lista_jugadores)
            print_space()
        case 17:
            valor = int(input("Ingrese un valor numérico porcentaje tiros triples por partido"))
            promedio_arriba_de_un_valor(lista_jugadores, valor ,ESTADISTICA_PORCENTAJE_TIROS_TRIPLES)
            print_space()
        case 18:
            buscar_jugador_mayor_por_campo(lista_jugadores, ESTADISTICA_TEMPORADA)
            print_space()
        case 19:
            nueva_lista = []
            valor = int(input("Ingrese un valor numérico porcentaje tiros de campo"))   
            nueva_lista = obtener_promedio_arriba_de_un_valor(lista_jugadores, valor, ESTADISTICA_PORCENTAJE_TIROS_DE_CAMPO)
            lista_ordenada = ordenar_listado_por_campo(nueva_lista, POSICION, "asc")
            for item in lista_ordenada:
                print(item[NOMBRE], item[POSICION], "- Valor ", item['valor'])  
            print_space()
        case 20:
            ruta = "parcial_dream\\csv\\bonus.csv"
            generar_bonus_csv(ruta, bonus(lista_jugadores))
            print_space() 
