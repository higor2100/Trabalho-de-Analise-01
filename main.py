from array import array


def maximo_entre_arrays(vet, inicio, meio, final):
    soma = 0
    esq = -float("inf")
    for i in range(meio, inicio - 1, -1):
        soma += vet[i]
        if soma > esq:
            esq = soma
            max_esq = i
    right_sum = -float("inf")
    soma = 0
    for j in range(meio + 1, final + 1):
        soma += vet[j]
        if soma > right_sum:
            right_sum = soma
            max_dir = j
    return max_esq, max_dir, esq + right_sum


def somaMaxima(vet, inicio, final):
    if inicio == final:
        return inicio, final, vet[inicio]
    else:
        meio = round((inicio + final) / 2 - 0.5)
        inicio_esq, final_esq, esq = somaMaxima(vet, inicio, meio)
        inicio_dir, final_dir, soma_dir = somaMaxima(vet, meio + 1, final)
        inicio, final, soma = maximo_entre_arrays(vet, inicio, meio, final)

        if esq >= soma_dir and esq >= soma:
            return inicio_esq, final_esq, esq
        elif soma_dir >= esq and soma_dir >= soma:
            return inicio_dir, final_dir, soma_dir
        else:
            return inicio, final, soma


if __name__ == '__main__':
    vec1 = [21, 10, -50, 2, 27, -16, -4, 10]
    vec2 = [-16, 20, -10, 12, 27, -6, -4, 8]
    print(somaMaxima(vec1, 0, 7))
    print(somaMaxima(vec2, 0, 7))