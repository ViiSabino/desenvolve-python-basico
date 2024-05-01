import random

def embaralhar_palavras(stri):
    stri = stri.split()
    for i in range(len(stri)):
        if len(stri[i]) > 3:
            middle = list(stri[i][1:-1])
            random.shuffle(middle)
            middle = "".join(middle)
            stri[i] = stri[i][0] + middle + stri[i][-1]
    stri = " ".join(stri)
    return stri

frase = input("Insira uma frase: ")
resultado = embaralhar_palavras(frase)
print("Frase embralhada -",resultado)