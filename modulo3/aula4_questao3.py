year = int(input("Insira o ano: "))

bissexto = (year%4 == 0 and year%100 != 0) or year%400 == 0
if bissexto == True:
    print("bissexto")
else:
    print("não bissexto")