import random
list = [random.randint(-10,10) for i in range(20)]
print("Original", list)

neg = []
for i in range(20):
    if list[i] < 0:
        neg.append(i)

inter = [0,0]
big = 0
for i in range(len(neg)):
    n = 1
    while i+n <= len(neg)-1:
        if neg[i+n] == neg[i]+n: 
            n+=1
            if n>big: 
                big=n
                inter[0] = neg[i]
                inter[1] = neg[i+n-1]
        else: break

del list[inter[0]:inter[1]+1]
print("Editada", list)