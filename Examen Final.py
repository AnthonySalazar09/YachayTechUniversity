#Final de Algoritmos
#Anthony Salazar 1.-

def animo(matriz,palabras):
    estados = [0 for i in range(len(matriz[0]))]
    for word in palabras:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j]==word.lower():
                    estados[j]+=1
    idx = 0
    mayor = estados[0]
    for i in range(len(estados)):
        if mayor<estados[i]:
            mayor = estados[i]
            idx = i
    return idx


matriz_estados = [
    ["contento","amor","obscuro"],
    ["lindo","quiero","silencio"],
    ["suerte","besos","extraño"],
    ["sonrisa","abrazo","feo"]
]

mensaje = input("Mensaje: ").split(" ")
estados = ["Felicidad","Amor","Miedo"]
print(estados[animo(matriz_estados,mensaje)])
