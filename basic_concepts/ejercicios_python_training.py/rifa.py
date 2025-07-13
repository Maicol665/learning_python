# Número ganador fijo
numero_ganador = 61

# Usamos un bucle para que el usuario siga intentando hasta que gane
while True:
    # Pedimos al usuario que ingrese su número de la suerte
    numero_usuario = int(input("Ingresa un número entre 1 y 100: "))

    # Verificamos si el número ingresado es el ganador
    if numero_usuario == numero_ganador:  # Comparación de los números
        print("¡Felicidades! Has ganado la rifa.")
        break  # Salimos del bucle si el número es el ganador
    else:
        print("Lo siento, sigue intentando.")