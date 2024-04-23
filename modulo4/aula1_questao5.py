n = int(input("Insira a quantidade de respondentes: "))
total = n
sum = 0
while n>0:
    age = int(input(f"Insira a {total - n + 1}ª idade: "))
    sum += age
    n -= 1
print(f"A média das idades é {(sum/total):.1f} ano(s).")