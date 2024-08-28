import json
import os
def cargar_palabras():    
    ruta_directorio = os.path.dirname(os.path.abspath(__file__))
    ruta_palabras = os.path.join(ruta_directorio, 'palabras.json')
    
    with open(ruta_palabras, 'r') as archivo:
        datos = json.load(archivo)
    return datos["palabras"]
