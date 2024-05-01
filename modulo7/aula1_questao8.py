def digit(n):
    mult = 2
    sum = 0
    for i in range(-1,-1*(len(n)+1),-1):
        sum += int(n[i])*mult
        mult += 1
    if sum%11 < 2: return 0
    else: return 11-(sum%11)

def validate(n):
    if len(n) != 11: return False

    test1 = n[0:-2]
    if digit(test1) != int(n[-2]): return False

    test2 = n[0:-1]
    if digit(test2) != int(n[-1]): return False
    
    return True

cpf = input("Insira um CPF válido (apenas números): ")
print("CPF válido") if validate(cpf) else print("CPF inválido")