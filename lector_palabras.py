import json
def cargar_palabras(nombre_archivo):
    """
    Carga las palabras desde un archivo JSON.

    Parámetros:
    nombre_archivo (str): El nombre del archivo JSON que contiene las palabras.

    Retorna:
    list: Una lista de palabras cargadas desde el archivo JSON.
    """
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos["palabras"]
