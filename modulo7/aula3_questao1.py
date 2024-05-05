import os

phrase = input("Insira uma frase: ")
with open("frase.txt","w") as f:
    f.write(phrase)
print("Frase salva em",os.path.abspath("frase.txt"))
