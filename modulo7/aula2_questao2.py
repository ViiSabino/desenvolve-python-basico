phrase = input("Insira uma frase: ")
for i in phrase:
    if i.lower() in "aeiou":
        phrase = phrase.replace(i,"*")
print("Frase modificada:",phrase)