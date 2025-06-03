N = int(input())

res = 0
for i in range(int(N**0.5)):
    if(N % (i+1) == 0):
        res = max(res, i+1)

print((res-1) + (N//res-1))
