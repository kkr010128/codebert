# C - Next Prime
N = 110000
p = [0]*N
x = int(input())

for i in range(2,N):
    if p[i]:
        continue
    if i>=x:
        print(i)
        break
    tmp = i
    while tmp<N:
        p[tmp] = 1
        tmp += i