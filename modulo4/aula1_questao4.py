n = int(input("Qual a quantidade de números? "))
maior = 0 
while n > 0:
    x = int(input("Insira o número: "))
    if x > maior:
        maior = x
    n -= 1
print("O maior valor é", maior)
