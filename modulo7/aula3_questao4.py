import random

def imprime_enforcado(n,lista):
    return print(lista[n]) 

def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

with open("gabarito_forca.txt") as f:
    lines = f.readlines()
word = lines[random.randint(0,len(lines)-1)]
word = word[:-1]

with open("gabarito_enforcado.txt") as f:
    forca = f.read()
forca = forca.split("\n")
templates = []
for i in range(7):
    templates.append([y for y in forca[i*6:i*6+5]])
    templates[i] = "\n".join(templates[i])

strikes = 0
game,guesses = ["_" for i in range(len(word))], []
while strikes < 6:
    print("")
    if len(guesses) > 0: print("Letras já testadas:", guesses) 
    imprime_enforcado(strikes,templates)
    for i in game: print(i,end="")
    print("")

    guess = input().lower()
    if guess in guesses:
        print("Essa letra já foi testada")
        continue
    guesses.append(guess)

    if guess in word: 
        for i in indices(word,guess):
            game[i] = word[i]        
    else: strikes += 1
    if "_" not in game: break
if strikes < 6: print("Você ganhou!") 
else:
    imprime_enforcado(strikes,templates)
    print("Você perdeu.")
print("A palavra era:",word)