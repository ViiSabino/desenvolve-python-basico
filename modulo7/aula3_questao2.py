import os

with open("frase.txt","r") as f:
    doc = f.read()
doc = doc.split()
doc = [i+"\n" for i in doc]
with open("palavras.txt","w") as f:
    f.writelines(doc)
for i in doc:
    print(i.rstrip()) 