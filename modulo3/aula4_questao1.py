num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
sum = num1 + num2

if sum%2 == 0:
    print(f"A soma dos números {num1} e {num2} é par.")
else:
    print(f"A soma dos números {num1} e {num2} é ímpar.")