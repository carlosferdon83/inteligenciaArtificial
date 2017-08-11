def validarFila(fila_aleatoria):
    encontrado = " "
    for fila in range(fila_aleatoria):
        for j in range(8):
            if(matriz[fila_aleatoria][j]=='R'):
                print "Se ha encontrado una reina en la posicion ",fila_aleatoria,j
                encontrado = "exito"
                break
    return encontrado
     

from random import randrange
numeroReinas = int(input("Introduce el numero de Reinas"))
contador = 1
matriz = []
columnas = 8
for filas in range(8):
    matriz.append([0]*columnas)
matriz[randrange(8)][randrange(8)] = 'R'
print "*****MATRIZ INICIAL*****"
print matriz    
while contador<=numeroReinas:
    fila_aleatoria = randrange(8)
    columna_aleatoria = randrange(8)
    resultado = validarFila(fila_aleatoria)
    if(resultado == "exito"):
        matriz[fila_aleatoria][columna_aleatoria] = 'X'
    else:
        matriz[fila_aleatoria][columna_aleatoria] = 'R'
    contador = contador + 1
print "*****MATRIZ FINAL*****"
print matriz