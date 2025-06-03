N = int(input())
C = {(i,j):0 for i in range(1,10) for j in range(1,10)}
num = list(range(1,10))
for k in range(1,N+1):
    k = str(k)
    i = int(k[0])
    j = int(k[-1])
    if i in num and j in num:
        C[(i,j)] += 1
cnt = 0
for i in range(1,10):
    for j in range(1,10):
        cnt += C[(i,j)]*C[(j,i)]
print(cnt)