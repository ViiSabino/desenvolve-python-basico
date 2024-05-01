date = input("Digite sua data de nascimento: ")
date = date.split("/")

months = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
date[1] = months[int(date[1]) - 1]

print(f"Você nasceu no dia {date[0]} de {date[1]} de {date[2]}")