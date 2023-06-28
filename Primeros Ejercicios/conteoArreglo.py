numbers = [10, 5, 7, 2, 1]
# Imprimiendo el contenido de la lista original.
print("Contenido de la lista original:", numbers)

numbers[0] = 111
# Imprimiendo contenido de la lista con 111.
print("\nContenido de la lista con cambio:", numbers)

# Copiando el valor del quinto elemento al segundo elemento.
numbers[1] = numbers[4]
# Imprimiendo contenido de la lista con intercambio.
print("Contenido de la lista con intercambio:", numbers)

# Imprimiendo la longitud de la lista.
print("\nLongitud de la lista:", len(numbers))

# Imprimiendo el arreglo completo
print('\n', numbers)
