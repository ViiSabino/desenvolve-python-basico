with open("spotify-2023.csv","r",encoding="latin-1") as f:
    doc = f.read().split("\n")

for i in range(len(doc)):
    doc[i] = doc[i].split(",")
        
    for y in range(len(doc[i])):
        if y < 2: continue
        if doc[i][y].isdigit():
            artist_count = int(doc[i][y])
            if artist_count > 1:
                if i == 23: print("osh, entrei")

                singers = ",".join(doc[i][y-artist_count:y])
                doc[i][y-artist_count:y] = [singers]

                singers = doc[i].index(singers)
                if singers != 1:
                    doc[i][:singers] = [",".join(doc[i][:singers])]
            else: 
                if y != 2: doc[i][:y-1] = [",".join(doc[i][:y-1])]
            break
    try: 
        doc[i][0] = doc[i][0].strip('"')
        doc[i][1] = doc[i][1].strip('"')
        del doc[i][2:3]
        del doc[i][3:7] 
        del doc[i][4:]
    except IndexError: del doc[i]

### 0 -> song
### 1 -> artist(s)
### 2 -> year
### 3 -> streaming

del doc [0:1]
for i in doc:
    if i[2] == "Arctic Monkeys": print(i,doc.index(i))

bests = [[] for _ in range(11)]
for i in doc:
    year = int(i[2]) - 2012
    if year < 0  or year > 10: continue
    try:
        if int(bests[year][3]) < int(i[3]): bests[year] = i
    except IndexError: bests[year] = i

for i in bests:print(i)