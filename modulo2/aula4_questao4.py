value = int(input("Digite o valor: "))
cent = value//100
fifs = (value - cent*100)//50
twents = (value - cent*100 - fifs*50)//20
dozens = (value - cent*100 - fifs*50 - twents*20)//10
fives = (value - cent*100 - fifs*50 - twents*20 - dozens*10)//5
twos = (value - cent*100 - fifs*50 - twents*20 - dozens*10 - fives*5)//2
ones = (value - cent*100 - fifs*50 - twents*20 - dozens*10 - fives*5 - twos*2)//1

print(f"{cent} nota(s) de R$100,00")
print(f"{fifs} nota(s) de R$50,00")
print(f"{twents} nota(s) de R$20,00")
print(f"{dozens} nota(s) de R$10,00")
print(f"{fives} nota(s) de R$5,00")
print(f"{twos} nota(s) de R$2,00")
print(f"{ones} nota(s) de R$1,00")