N = int(input())
A=list(map(int,input().split()))
sumxor=0
for i in range(N):
    sumxor=sumxor^A[i]
for i in range(N):
    print(sumxor^A[i],"",end='')
print()