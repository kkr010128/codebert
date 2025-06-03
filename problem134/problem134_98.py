N = int(input())
A = list(map(int, input().split()))

A = sorted(A)
result=1
max=10**18
for a in A:
    result *= a
    if result>max:
        print(-1)
        break
else:
    print(result)