N = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

k = 2**N
totallist = [0]*k
for b in range(k):
    total = 0
    for i in range(N):
        if b >> i & 1 == 1:
            total += A[i]
    totallist[b] = total

for m in M:
    print('yes') if m in totallist else print('no')
