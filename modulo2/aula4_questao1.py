# captação de dados do terreno em inteiro
lengh = int(input("Digite o comprimento do terreno: "))
width = int(input("Digite a largura do terreno: "))

# captação do dado do preço da região
price_m2 = float(input("Digite o preço por m² da região: "))

# calculos de área e preço
area = lengh*width
price = area*price_m2

# retorno de dados
print(f"O terreno possui {area}m² e custa R${price:,.02f}")