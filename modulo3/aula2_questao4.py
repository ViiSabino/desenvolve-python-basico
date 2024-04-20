classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
strengh = int(input("Digite os pontos de força: "))
magic = int(input("Digite os pontos de magia: "))

print(f"Pontos de atributo consistentes com a classe escolhida: {not((classe ==  "guerreiro" and (strengh < 15 or magic > 10)) or (classe == "mago" and (strengh > 10 or magic < 15)) or (classe == "arqueiro" and (strengh < 5 or magic < 5 or strengh > 15 or magic > 15)))}")