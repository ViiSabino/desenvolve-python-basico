urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
doms = []
for i in urls:
    doms.append(i[4:-4])
print("Domínios:", doms)
