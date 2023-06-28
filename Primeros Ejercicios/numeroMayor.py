# Definimos la variable y la inicializamos con un valor
numeroMasGrande = -999999999999

# Inicializamos la variable "numero" donde se almacena el numero ingresado por pantalla
numero = int(
    input('Ingresa un número o ingresa -1 para detener el programa: '))

# Creamos el bucle, mientras el numero ingresado sea diferente a -1
while numero != -1:

    # Si el numero (numero ingresado por pantalla) es mayor que la variable numeroMasGrande
    if numero > numeroMasGrande:

        # Entonces ahora el numeroMasGrande ahora es el ingresa por la variable "numero"
        numeroMasGrande = numero

    # Mientra el valor sea diferente de -1, sigue solicitando el ingreso de numeros
    numero = int(
        input('Ingresa un número o ingresa -1 para detener el programa: '))

# Cuando ingresen -1, el bucle finaliza y muestra este mensaje junto con el numero mas grande ingresado
print('El numero mas grande ingresado fue: ', numeroMasGrande)
