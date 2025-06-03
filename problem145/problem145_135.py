n,m = map(int, input().split())
neighbors = {key:[] for key in range(1, n+1)}
answers = {key:0 for key in range(1, n+1)}
answers[1] = 1
for i in range(m):
    a,b = map(int, input().split())
    neighbors[a].append(b)
    neighbors[b].append(a)

def register(hs):
    newhs = []
    for h in hs:
        for i in neighbors[h]:
            if answers[i] == 0:
                answers[i] = h
                newhs.append(i)
    return newhs

hosts = [1]
while True:
    hosts = register(hosts)
    if len(hosts) == 0:
        break

flag = 0
for key, item in answers.items():
    if item == 0:
        flag = 1
if flag == 0:
    print("Yes")
    for key, item in answers.items():
        if key != 1:
            print(item)
else:
    print("No")