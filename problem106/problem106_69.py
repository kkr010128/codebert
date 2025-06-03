import itertools

N = int(input())

tbl = [0]*N

for x in range(1,N):
    for y in range(1,N):
        for z in range(1,N):
            p = x*x + y*y + z*z + x*y + y*z + z*x
            if p > N:
                break
            tbl[p-1] += 1

for i in range(N):
    print(tbl[i])
