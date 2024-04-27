while True:
    n = int(input("Digite o tamanho da lista, com mínimo 4: "))
    if n < 4: print("Insira um valor maior que 4")
    else: break
list = []
for i in range(n):
    list.append(int(input()))

print("A lista original é:", list)
print("Os três primeiros elementos são:", list[:3])
print("Os dois últimos elementos são:", list[:-3:-1])
print("A lista invertida é:", list[::-1])
print("Os elementos de índice par são:", list[::2])
print("Os elementos de índice ímpar são:", list[1::2])
