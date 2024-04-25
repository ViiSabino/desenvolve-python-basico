import math
import random


n = int(input("Digite a quantidade: "))
sum = 0
for i in range(n):
    sum += random.randint(0,100)
print (f"A raiz da soma é {math.sqrt(sum):.2f}.")