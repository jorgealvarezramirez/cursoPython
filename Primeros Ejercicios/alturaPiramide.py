blocks = int(input("Ingresa el número de bloques: "))

height = 0
total_blocks = 0

while total_blocks < blocks:
    height += 1  # Incrementa la altura de la pirámide en 1
    # Suma la cantidad de bloques utilizados en la capa actual a total_blocks
    total_blocks += height

    if total_blocks > blocks:
        height -= 1  # Reduce la altura en 1 si se supera la cantidad de bloques disponibles
        break

print("La altura de la pirámide:", height)
