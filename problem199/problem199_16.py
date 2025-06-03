t = ""
D = set([])
for _ in range(5):
    t += "hi"
    D.add(t)
print("Yes" if input() in D else "No")