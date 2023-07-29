db = open("database.txt", "r")
d = []
f = []
for i in db:
    a,b= i.split(", ")
    b = b.strip()
    d.append(a)
    f.append(b)
data = dict(zip(d, f))
print(data)