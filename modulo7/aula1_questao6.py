def is_anagram(obj,word):
    if not len(word) == 4: return False
    for letter in word:
        if letter not in obj: return False
    return True
        
phrase = input("Digite uma frase: ")
word = input("Digite a palavra objetivo: ")
word += word.upper()

phrase = phrase.split()
for i in range(len(phrase)):
    phrase[i] = list(phrase[i])

anagrams = []
for i in phrase:
    if is_anagram(word,i):
        join = ""
        for y in i:
            join += y
        anagrams.append(join)

print("Anagramas:", anagrams)