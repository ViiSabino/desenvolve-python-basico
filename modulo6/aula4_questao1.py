l1 = [i for i in range(20,51) if i%2==0]
print(l1)

l2 = [i**2 for i in [1,2,3,4,5,6,7,8,9]]
print(l2)

l3 = [i for i in range (1,101) if i%7==0]
print(l3)

l4 = ["par" if i%2==0 else "ímpar" for i in range(0,30,3)]
print(l4)