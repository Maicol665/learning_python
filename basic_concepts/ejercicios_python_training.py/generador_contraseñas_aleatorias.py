import random
import string

longitud = int(input("Longitud de la contraseña: "))

caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))

print(f"Tu contraseña segura es: {contraseña}")