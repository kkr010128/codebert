n,k,c = list(map(int, input().split()))
s = input()
ls = list(s)

ortho = [0]*k
rever = [0]*k

a = 0
skip = []
for i in range(len(ls)):
    if a >= k: break
    if ls[i] == "o" and i not in skip:
        ortho[a] = i
        a += 1
        skip = [i+j for j in range(1, c+1)]

a = 0
skip = []
ls.reverse()
for i in range(len(ls)):
    if a >= k: break
    if ls[i] == "o" and i not in skip:
        rever[a] = i
        a += 1
        skip = [i+j for j in range(1, c+1)]

rever.reverse()
rever = [len(ls)-1-i for i in rever]

for i in range(k):
    if ortho[i] == rever[i]:
        print(ortho[i]+1)