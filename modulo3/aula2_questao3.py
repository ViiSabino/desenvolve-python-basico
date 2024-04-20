age = int(input("Qual sua idade? "))
games = bool(input("Você já jogou pelo menos 3 jogos de tabuleiro? "))
wins = int(input("Quantas vezes você já venceu um jogo? "))

print(f"Apto para ingressar no clube de jogos de tabuleiro: {(age <= 18 and age >= 16) and (games == True) and (wins >= 1)}")