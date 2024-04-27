phrase = input("Insira uma frase: ")
vogals = [i for i in phrase if i in ["a","A","e","E","i","I","o","O","u","U"]]
consonants = [i for i in phrase if not i in ["a","A","e","E","i","I","o","O","u","U"," "]]

print("Vogais:", sorted(vogals))
print("Consoantes", consonants)