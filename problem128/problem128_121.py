x, n = map(int, input().split())
p = list(map(int, input().split()))

l = [i - x for i in p]
m = [0]
for i in range(1, 101):
    m.append(-i)
    m.append(i)
for i in range(201):
    if (m[i] in l) == True:
        continue
    if (m[i] in l) == False:
        print(x + m[i])
        break