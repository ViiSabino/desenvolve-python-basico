def is_palindrome(str):
    str = ("".join(x for x in str if x.isalpha())).lower()
    if str != str[::-1]: return False
    return True

while True:
    phrase = input("Digite uma frase (digite 'Fim' para encerrar): ")
    if phrase == "Fim": break
    print(f"'{phrase}' é palíndromo") if is_palindrome(phrase) else print(f"'{phrase}' não é palíndromo")