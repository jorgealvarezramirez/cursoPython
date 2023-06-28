conteoNumerosImpares = 0
conteoNumerosPares = 0

numero = int(input('Ingrese un número, cero finaliza el programa '))

while numero != 0:  # Mientras numero sea diferente de cero haga la siguiente
    # Si el resto de numero(numero ingresado)es igual a 1, entonces es un numero impar
    if numero % 2 == 1:

        # Entonces incrementamos el conteo en uno la variable "conteoNumerosImpares"
        conteoNumerosImpares += 1

    # Si no es impar entonces con defecto es par, entonces incrementamos la variables de par
    else:
        conteoNumerosPares += 1

    # Continuando con el bucle, si no digitan cero
    numero = int(input('Ingrese un número, cero finaliza el programa '))

    # Si digitan cero para terminar el programa, mostramos el contep final de numero pares e impares

print('Resultado final conteo de número pares: ', conteoNumerosPares)
print('Resultado final conteo de número impares: ', conteoNumerosImpares)

# Ojo los print finales deben estar fuera del bucle, de lo contrario el programa
# da error. Cuidado con le identación
