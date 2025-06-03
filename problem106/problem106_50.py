N = int(input())
C = {i:0 for i in range(1,N+1)}
for x in range(1,142):
    for y in range(1,142):
        for z in range(1,142):
            a = (x+y)**2+(y+z)**2+(z+x)**2
            if a%2==0 and a//2<=N:
                C[a//2] += 1
for i in range(1,N+1):
    print(C[i])
