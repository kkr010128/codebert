X = int(input())
N = X//100
X %=100
if N == 0:
    print(0)
    exit()
if X == 0:
    print(1)
    exit()
for i in [5,4,3,2,1]:
    for j in range(N,0,-1):
        if X//(i*j) > 0:
            N -= j
            X %= i*j
            break
    if N == 0:
        break
if X == 0:
    print(1)
else:
    print(0)