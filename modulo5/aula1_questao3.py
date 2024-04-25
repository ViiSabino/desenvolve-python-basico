import random

n = random.randint(1,10)
while True:
    guess = int(input("Adivinhe o número de 1 a 10: "))
    if guess == n: break
    elif guess < n: print("Muito baixo, tente novamente!")
    elif guess > n: print("Muito alto, tente novamente!")
print(f"Correto! O número é {n}")