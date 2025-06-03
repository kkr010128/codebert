[N, K] = list(map(int, input().split()))
P = list(map(int, input().split()))
P.sort(reverse=True)

total = 0
for i in range(K):
    total += P.pop()

print (total)


