gender = input("Insira seu gênero (M ou F): ")
age = int(input("Insira sua idade: "))
time = int(input("Insira seu tempo de serviço: "))

print(f"Apto a se aposentar: {(gender == "M" and age >= 65) or (gender == "F" and age >= 60 ) or (time >= 30) or (age >= 60 and time >= 25)}")