from lector_palabras import cargar_palabras
from ahorcado import mostrar_ahorcado
import warnings
import pandas as pd
import time
import json
import random
warnings.simplefilter(action='ignore', category=FutureWarning)

def mostrar_tablero(palabra, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

def registrar_estadisticas(df, palabra, intentos_fallidos, tiempo_total, resultado, puntaje):
    nueva_fila = {
        "Palabra": palabra,
        "Intentos Fallidos": intentos_fallidos,
        "Duración (s)": tiempo_total,
        "Resultado": resultado,
        "Puntaje Acumulado": puntaje
    }

    nueva_fila_df = pd.DataFrame([nueva_fila])
    
    # Eliminar columnas que son completamente NaN o vacías antes de la concatenación
    nueva_fila_df = nueva_fila_df.dropna(axis=1, how='all')

    # Concatenar el DataFrame original con la nueva fila
    return pd.concat([df, nueva_fila_df], ignore_index=True)

def ahorcado():
    try:
        palabras = cargar_palabras()
    except FileNotFoundError:
        print("Error: El archivo 'palabras.json' no fue encontrado.")
        return
    except json.JSONDecodeError:
        print("Error: El archivo 'palabras.json' tiene un formato incorrecto.")
        return    
    puntaje = 0    
    seguir_jugando = True
    estadisticas = pd.DataFrame(columns=["Palabra", "Intentos Fallidos", "Duración (s)", "Resultado", "Puntaje Acumulado"])


    #! Ciclo principal del juego
    while seguir_jugando:
        palabra = random.choice(palabras)  # Selecciona una palabra al azar
        letras_adivinadas = set()  # Conjunto de letras que el jugador ha adivinado
        intentos = 6  # Número máximo de intentos
        palabra_adivinada = False  # Estado de la palabra adivinada
        intentos_fallidos = 0
        inicio_tiempo = time.time()

        print("¡Bienvenido al juego del ahorcado!")
        
        #! Ciclo interno para cada palabra
        while intentos > 0 and not palabra_adivinada:
            print(mostrar_ahorcado(intentos))  # Muestra la figura del ahorcado            
            print("\n" + mostrar_tablero(palabra, letras_adivinadas))  # Muestra el estado actual del tablero
            
            try:            
                intento = input(f"Tienes {intentos} intentos restantes. Ingresa una letra: ").lower()
            except Exception as e:
                print(f"Error en la entrada: {e}")
                continue
            
            #? Validación de entrada
            
            if len(intento) != 1 or not intento.isalpha():
                print("Entrada no válida. Por favor, ingresa solo una letra.")
                continue
            
            #? Verifica si la letra ya fue adivinada
            if intento in letras_adivinadas:
                print("Ya has adivinado esa letra.")
                continue
            
            letras_adivinadas.add(intento)  #! Agrega la letra al conjunto de letras adivinadas
            
            #? Verifica si la letra está en la palabra
            if intento in palabra:
                print("¡Correcto!")
            else:
                intentos -= 1  #! Reduce los intentos restantes
                intentos_fallidos +=1
                print(f"Incorrecto. Te quedan {intentos} intentos.")
            
            #! Verifica si el jugador ha adivinado toda la palabra
            if all(letra in letras_adivinadas for letra in palabra):
                palabra_adivinada = True
                print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
                puntaje += 1  # Incrementa el puntaje
        
        #! Si el jugador no adivinó la palabra
        if not palabra_adivinada:
            print(mostrar_ahorcado(0))  # Muestra la figura completa del ahorcado
            print(f"Has perdido. La palabra era: {palabra}")
            
        duracion_juego = time.time() - inicio_tiempo
        resultado = "Ganar" if palabra_adivinada else "perder"
        
        #!Regustrar estadistica del juego
        estadisticas = registrar_estadisticas(estadisticas, palabra, intentos_fallidos, duracion_juego, resultado, puntaje)

        print(f"Tu puntaje actual es: {puntaje}")
        
        #? Pregunta si el jugador quiere seguir jugando
        while True:
            jugar_otra_vez = input("¿Quieres seguir jugando? (si/no): ").lower()
            if jugar_otra_vez in ['si', 'no']:
                break
            print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")

        #! Verifica si el jugador decide dejar de jugar
        if jugar_otra_vez == 'no':
            seguir_jugando = False
            print(f"Gracias por jugar. Tu puntaje final es: {puntaje}")
            
#! Guardar las estadísticas en un archivo CSV
    estadisticas.to_csv('estadisticas_ahorcado.csv', index=False)
    print("Las estadísticas del juego han sido guardadas en 'estadisticas_ahorcado.csv'.")

if __name__ == "__main__":
    try:
        ahorcado()
    except Exception as e:
        print(f"Error critico: {e}")
