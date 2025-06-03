N = int(input())
li = [[0]*9 for i in range(9)]
counter = 0

for i in range(1,N+1):
    I = str(i)
    fast = int(I[0])
    last = int(I[-1])
    if not last==0:
        li[fast-1][last-1] += 1

for i in range(9):
    for k in range(9):
        counter += li[i][k]*li[k][i]


print(counter)