with open("estomago.txt") as f:
    lines = f.readlines()
print("25 primeiras linhas:")

for i in lines[:25]:
    print(i.rstrip())

quant_lines = 0
for i in lines:
    quant_lines += 1
print("Quantidade de linhas do documento:", quant_lines)

lines.sort(key=lambda n:len(n))
print("Linha com maior número de caracteres:", lines[-1])

nonato = 0
iria = 0
for i in lines:
    if "nonato" in i.lower().split(): nonato += 1
    if "íria" in i.lower().split(): iria += 1
print("Menções a Nonato:", nonato)
print("Menções a Íria:", iria)