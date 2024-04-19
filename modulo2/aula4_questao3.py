product1 = input("Digite o nome do produto 1: ")
price1 = float(input("Digite o preço do produto 1: "))
quant1 = int(input("Digite a quantidade do produto 1: "))
product2 = input("Digite o nome do produto 2: ")
price2 = float(input("Digite o preço do produto 2: "))
quant2 = int(input("Digite a quantidade do produto 2: "))
product3 = input("Digite o nome do produto 3: ")
price3 = float(input("Digite o preço do produto 3: "))
quant3 = int(input("Digite a quantidade do produto 3: "))

total = (price1*quant1) + (price2*quant2) + (price3*quant3)

print(f"Total R${total:,.2f}")