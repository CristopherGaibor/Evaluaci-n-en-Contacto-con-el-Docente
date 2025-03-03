import random

# Lista de palabras con sus respectivas pistas
palabras_y_pistas = [
    ("python", "Un lenguaje de programación muy popular"),
    ("guitarra", "Instrumento de cuerdas común en la música"),
    ("amazonas", "El río más largo del mundo"),
    ("tigre", "Un felino grande con rayas negras"),
    ("montaña", "Una elevación natural del terreno"),
    ("luna", "El satélite natural de la Tierra"),
    ("volcán", "Una montaña que expulsa lava"),
    ("avión", "Un medio de transporte aéreo"),
    ("planeta", "Cuerpo celeste que orbita una estrella"),
    ("salsa", "Baile latinoamericano o una comida deliciosa"),
]

def jugar():
    print("¡Bienvenido al juego de adivinanzas de palabras!")
    print("Recibirás una pista y tendrás que adivinar la palabra correspondiente.")
    print("Escribe 'salir' si quieres terminar el juego.\n")
    
    puntuacion = 0

    while True:
        # Elegir una palabra y su pista al azar
        palabra, pista = random.choice(palabras_y_pistas)

        print(f"Pista: {pista}")
        intento = input("¿Cuál es la palabra? ").lower()
        
        if intento == "salir":
            print(f"\nJuego terminado. Tu puntuación final es: {puntuacion}")
            break

        if intento == palabra:
            print("¡Correcto! 🎉\n")
            puntuacion += 1
        else:
            print(f"Incorrecto. La palabra era: {palabra}.\n")

# Llamar a la función principal
jugar()
