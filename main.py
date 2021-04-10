def maximoEntreListas(v, i, m, f):
    # i = inicio; f = final, m = meio, v = vetor
    s = 0
    #s = Soma
    e = -float("inf")
    #e = Esquerda
    for j in range(m, i - 1, -1):
        s += v[j]
        if s > e:
            e = s
            mE = j
            #mE = Maximo Esquerdo
    dS = -float("inf")
    #Soma a Direita
    s = 0
    for j in range(m + 1, f + 1):
        s += v[j]
        if s > dS:
            dS = s
            mD = j
            #Maximo a Direita
    return mE, mD, e + dS


def somaDoMaxima(v, i, f):
    if i == f:
        return i, f, v[i]
    else:
        m = round((i + f) / 2 - 0.5)
        iE, fE, e = somaDoMaxima(v, i, m)
        #iE = inicio a esquerda; fE = final a esquerda, e = esquerda
        iD, fD, sD = somaDoMaxima(v, m + 1, f)
        #iD = inicio a direita; fD = final a direita, d = direita
        i, f, s = maximoEntreListas(v, i, m, f)

       
        if sD >= e and sD >= s:
            #sD =soma direta
            return iD, fD, sD
        elif e >= sD and e >= s:
            return iE, fE, e
        else:
            return i, f, s

vec1 = [10, 13, -30, 1, 25, -8, -14, 1]
vec2 = [-16, 20, -10, 12, 27, -6, -4, 8]
print(somaDoMaxima(vec1, 0, 7))
print(somaDoMaxima(vec2, 0, 7))