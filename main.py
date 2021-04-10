def maximoEntreListas(vet, inicio, meio, final):
    soma = 0
    esq = -float("inf")
    for i in range(meio, inicio - 1, -1):
        soma += vet[i]
        if soma > esq:
            esq = soma
            maxEsq = i
    dirSoma = -float("inf")
    soma = 0
    for j in range(meio + 1, final + 1):
        soma += vet[j]
        if soma > dirSoma:
            dirSoma = soma
            maxDir = j
    return maxEsq, maxDir, esq + dirSoma


def somaMaxima(vet, inicio, final):
    if inicio == final:
        return inicio, final, vet[inicio]
    else:
        meio = round((inicio + final) / 2 - 0.5)
        inicioEsq, finalEsq, esq = somaMaxima(vet, inicio, meio)
        inicioDir, finalDir, somaDir = somaMaxima(vet, meio + 1, final)
        inicio, final, soma = maximoEntreListas(vet, inicio, meio, final)

       
        if somaDir >= esq and somaDir >= soma:
            return inicioDir, finalDir, somaDir
        elif esq >= somaDir and esq >= soma:
            return inicioEsq, finalEsq, esq
        else:
            return inicio, final, soma

vec1 = [10, 13, -30, 1, 25, -8, -14, 1]
vec2 = [-16, 20, -10, 12, 27, -6, -4, 8]
print(somaMaxima(vec1, 0, 7))
print(somaMaxima(vec2, 0, 7))