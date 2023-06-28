numeroSecreto = 8

while True:

    numero = int(
        input('Ingresa el número que sellará tu destino: '))

    if numero == numeroSecreto:
        print(numero, '¡Bien hecho, muggle! Eres libre ahora.')
        break

    else:
        print('¡Ja, ja! ¡Estás atrapado en mi bucle!')
