def validador_senha(senha):
    if len(senha) < 8: return False

    cap = 0
    for i in senha:
        if ord(i) < 91 and ord(i) > 64: cap = 1
    if cap == 0: return False
    
    min = 0
    for i in senha:
        if ord(i) < 123 and ord(i) > 96: min = 1
    if min == 0: return False

    num = 0
    for i in senha:
        if ord(i) < 58 and ord(i) > 47: num = 1
    if num == 0: return False

    char = 0
    for i in senha:
        if ord(i) < 48 and ord(i) > 32: char = 1
        if ord(i) < 65 and ord(i) > 57: char = 1
        if ord(i) < 97 and ord(i) > 90: char = 1
        if ord(i) < 127 and ord(i) > 122: char = 1
    if char == 0: return False
    
    return True

passw = input("Insira sua senha: ")
print("Senha válida") if validador_senha(passw) else print("Senha inválida")