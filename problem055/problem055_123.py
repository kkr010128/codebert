towers = [
    [[0 for i in range(10)] for j in range(3)] for k in range(4)
]
floor = 3

n = int(input())
for i in range(n):
    b,f,r,v = list(map(int,input().split()))
    towers[b-1][f-1][r-1] += v

for b in towers:
    for f in b:
        for r in f:
            print(' ' + str(r), end='')
        print('')
    if floor:
        print('#'*20)
        floor -= 1