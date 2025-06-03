n = int(input())

tenant = [
    [ [0]*10, [0]*10, [0]*10, ],
    [ [0]*10, [0]*10, [0]*10, ],
    [ [0]*10, [0]*10, [0]*10, ],
    [ [0]*10, [0]*10, [0]*10, ]
]


for i in range(n):
    b,f,r,nu = map(int, input().split())
    tenant[b-1][f-1][r-1] += nu

for b in range(4):
    for f in range(3):
        print(' ', end='')
        print(' '.join(map(str,tenant[b][f])))
    if b < 3:
        print('#'*20)