# Esta es una lista existente de números ocultos en el sombrero.
hat_list = [1, 2, 3, 4, 5]

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
print('\n', hat_list)
hat_list[2] = float(input("Ingresa el primer valor: "))
print('\n', hat_list)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]
print('\n', hat_list)

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print(len(hat_list))
