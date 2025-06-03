N = int(input())
As = list(map(int, input().split()))

isOKs = [False] * (N+1)
isOKs[0] = True
for A in As:
    if isOKs[A-1]:
        isOKs[A] = True

for A in reversed(range(1, N+1)):
    if isOKs[A]:
        print(N-A)
        break
else:
    print(-1)
