bldgs = []
for k in range(4):
    bldgs.append([[0 for i in range(10)] for j in range(3)])

n = int(input())
for i in range(n):
    b,f,r,v = map(int, input().split(' '))
    bldgs[b-1][f-1][r-1] += v

for i, bldg in enumerate(bldgs):
    if i > 0:
        print('#'*20)

    for floor in bldg:
        print(' '+' '.join([str(f) for f in floor]))