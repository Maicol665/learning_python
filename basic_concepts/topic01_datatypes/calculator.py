operacion = input("¿Qué operación deseas realizar? Escribe 'sumar', 'restar', 'multiplicar' o 'dividir': ").lower()

num1 = input("Ingresa un número: ")
num2 = input("Ingresa otro número: ")

num1 = float(num1)
num2 = float(num2)

if operacion == "sumar":
    result = num1 + num2
    print("El resultado de la suma es:", result)

elif operacion == "restar":
    result = num1 - num2
    print("El resultado de la resta es:", result)

elif operacion == "multiplicar":
    result = num1 * num2
    print("El resultado de la multiplicación es:", result)

elif operacion == "dividir":
    if num2 != 0:
        result = num1 / num2
        print("El resultado de la división es:", result)
    else:
        print("Error: No se puede dividir por 0.")

else:
    print("Operación no válida. Por favor, elige 'sumar', 'restar', 'multiplicar' o 'dividir'.")

dsfdsfsdfsdf