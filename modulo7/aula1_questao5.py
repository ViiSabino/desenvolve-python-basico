phrase = input("Digite uma frase: ")
vogals = 0
indexes = []
for i in phrase:
    if i in "aeiouAEIOU":
        vogals += 1
        indexes.append(phrase.index(i))
print(vogals,"vogais")
print("Índices:", indexes)