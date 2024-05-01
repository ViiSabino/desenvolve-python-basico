import random

def encrypt(l, n):
    for i in range(len(l)):
        l[i] = list(l[i])
        join = ""
        for letter in range(len(l[i])):
            l[i][letter] = chr(ord(l[i][letter])+n)
            join += l[i][letter]
        l[i] = join
    return l

names = ["Luana","Ju","Davi","Vivi","Pri","Luis"]
print("Nomes =", names)
key = random.randint(1,10)
print("Chave aleatória =", key)

names = encrypt(names,key)
print("Nomes cript =", names)
