n=int(input())
*l,=map(int, input().split())
solv=0
max=max(l) +1
count=[0 for i in range(max)]
for i in l:
    for j in range(i,max,i):
        count[j] += 1
for k in l:
    if count[k] == 1:
        solv += 1
print(solv)