



def obtener_preguntas():
    url = "https://opentdb.com/api.php?amount=15&category=21&difficulty=easy&type=multiple"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()['results']
    else:
        print("Error al obtener las preguntas.")
        return []



def mostrar_pregunta(pregunta, opciones):
    print(f"\n{pregunta}")
    for idx, opcion in enumerate(opciones, 1):
        print(f"{idx}. {opcion}")



def iniciar_juego():
    print("Bienvenido a ¿Quieres ser millonario?")
    nombre = input(" ingresa tu nombre: ")
    print(f"Hola, {nombre}. ¡Comencemos!")

    preguntas = obtener_preguntas()
    if not preguntas:
        print("No se pudieron cargar las preguntas. El juego no puede continuar.")
        return

    puntuacion = 0
    comodin_usado = False
    pregunta_actual = 0

    while pregunta_actual < len(preguntas):
        pregunta = preguntas[pregunta_actual]
        enunciado = pregunta['question']
        opciones = pregunta['incorrect_answers'] + [pregunta['correct_answer']]
        random.shuffle(opciones)

        print(f"\nPregunta {pregunta_actual + 1}:")
        mostrar_pregunta(enunciado, opciones)


        if not comodin_usado:
            usar_comodin = input("¿Quieres usar el comodín? (si/no): ")
            if usar_comodin.lower() == 'si':
                comodin_usado = True
                print("Comodín usado. La pregunta será saltada.")
                pregunta_actual += 1
                continue


        respuesta = input("Elige una opción (1-4) o escribe 'plantarme' para salir: ")

        if respuesta.lower() == 'plantamse':
            print(f"El juego ha finalozado con {puntuacion} puntos.")
            break

        if respuesta.isdigit() and 1 <= int(respuesta) <= 4:
            respuesta_idx = int(respuesta) - 1
            if opciones[respuesta_idx] == pregunta['correct_answer']:
                puntuacion += 1
                print(f"¡Correcto! Puntos actuales: {puntuacion}")
            else:
                print("¡Incorrecto paquete! Has perdido.")
                puntuacion = 0
                break
        else:
            print("Opción no válida. Prueba de nuevo.")
            continue

        pregunta_actual += 1

    if puntuacion > 0:
        print(f"\n¡Has terminado el juego con {puntuacion} puntos!")
    else:
        print("El juego ha terminado. Tu puntuación es 0.")


if __name__ == "__main__":
    iniciar_juego()






