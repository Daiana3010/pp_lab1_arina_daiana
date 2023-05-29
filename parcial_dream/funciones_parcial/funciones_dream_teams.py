import re
import json

def leer_archivo()->list:
    '''
    Esta función lee un archivo json y asigna el listado de heroes a la variable lista heroes.
    '''
    with open("parcial_dream\datos\dt_dream_teams.json", 'r') as archivo:
        diccionario = json.load(archivo)
    return diccionario["jugadores"]



