N = int(input())
alpha=list('abcdefghijklmnopqrstuvwxyz')
res=['']
for i in range(N):
    tmp = []
    for j in res:
        for k in alpha[:len(set(list(j))) +1]:
            tmp.append(j+k)
    res = tmp

for i in res:
    print(i)