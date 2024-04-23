n = int(input("Insira a quantidade de experimentos: "))
s = 0
r = 0
c = 0
while n>0:
    quant = int(input("Insira a quantidade de cobaias: "))
    type = input("Insira o tipo de cobaia: ")
    if type == "S":
        s += quant
    elif type == "R":
        r += quant
    elif type == "C":
        c += quant
    n -=1

print(f"Total: {s+r+c} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {(c/(s+r+c)*100):.2f}%")
print(f"Percentual de ratos: {(r/(s+r+c)*100):.2f}%")
print(f"Percentual de sapos: {(s/(s+r+c)*100):.2f}%")