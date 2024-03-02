## contraseña correcta ---
# min 8 caracteres y max 12
# al menos una meyuscula
# que contenga números
import re

def evaluarContrasenya(password):
    longitud_minima = 8
    longitud_maxima = 12
    num_caracteres = len(password)

    longitud = bool(num_caracteres in range(longitud_minima, longitud_maxima + 1, 1))
    mayus = bool(re.search(r'[A-Z]', password))
    minus = bool(re.search(r'[a-z]', password))
    numeros = bool(re.search(r'\d', password))

    # manejador de respuestas para verificar condiciones faltantes
    if not mayus:
        print("- La contraseña debe tener al menos una mayúscula")
    if not minus:
        print("- La contraseña debe tener al menos una minúsculas")
    if not longitud:
        if num_caracteres <= 8:
            print(f'- La contraseña debe tener al menos 8 caracteres\n   Número de caracteres usados: {num_caracteres}')
        if num_caracteres > 12:
            print(f'- La contraseña debe tener menos de 12 caracteres\n   Número de caracteres usados: {num_caracteres}')
    if not numeros:
        print("- La contraseña debe tener al menos un número")

    # imprimo el resultado evaluando si todas las condiciones son verdaderas
    return longitud and numeros and (mayus or minus)

contraseña = evaluarContrasenya(input("Introduzca su nueva contraseña: "))
buena_pass = 'Contraseña adecuada' if contraseña else 'la contraseña no cumple con los parametros de seguridad'

print(buena_pass)