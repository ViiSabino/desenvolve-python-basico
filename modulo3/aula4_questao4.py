distance = float(input("Insira a distância da entrega em km: "))
weight = float(input("Insira o peso do pacote em kg: "))

if distance <= 100:
    price = weight
if distance > 100 and distance <= 300:
    price = weight*1.5
if distance > 300:
    price = weight*2
if weight > 10:
    price += 10

print(f"O preço do frete será R${price:,.2f}.")