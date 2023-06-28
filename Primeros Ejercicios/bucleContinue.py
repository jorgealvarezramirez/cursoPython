# Ingreso de pabra y almecenado de la misma en la variable "palabraIngresada"
palabraIngresada = input('Ingresa una palabra: ')

# Metodo para pasar a mayusculas las palabras ingresadas
palabraIngresada = palabraIngresada.upper()

# Creamos en bucle for para recorrer la palabra ingresada y omite las vocales
for letter in palabraIngresada:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue

    print(letter)
