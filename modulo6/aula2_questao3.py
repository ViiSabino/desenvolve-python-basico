import random

list1 = []
list2 = []
for i in range(20):
    list1.append(random.randint(0,50))
    list2.append(random.randint(0,50))

common = []
for i in range(20):
    if list1[i] in list2 and not(list1[i] in common):common.append(list1[i]) 
common.sort()

print("Lista 1 -",list1)
print("Lista 2 -",list2)
print("Interseccao -", common)
print("Contagem")
for i in range(len(common)):
    print(f"{common[i]} - (lista 1 = {list1.count(common[i])}, lista 2 = {list2.count(common[i])})")