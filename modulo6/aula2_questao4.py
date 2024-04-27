n = int(input("Insira a quantidade de elementos da lista 1:"))
print("Insira os elementos da lista 1:")
list1 = []
for n in range(n):
    list1.append(int(input()))

n = int(input("Insira a quantidade de elementos da lista 2:"))
print("Insira os elementos da lista 1:")
list2 = []
for n in range(n):
    list2.append(int(input()))

switch = []
big = lambda l1,l2: l1 if len(l1)>len(l2) else l2
small = lambda l1,l2: l1 if len(l1)<len(l2) else l2
dif = lambda l1,l2:len(big(l1,l2))-len(small(l1,l2))

for i in range (len(small(list1,list2))):
        switch.append(list1[i])
        switch.append(list2[i])
if dif(list1,list2) != 0:
    for i in range (dif(list1,list2)):
         switch.append(big(list1,list2)[len(small(list1,list2))+i])
print("Lista intercalada:", switch)