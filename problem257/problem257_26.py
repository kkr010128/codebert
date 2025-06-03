N = int(input())
A = list(map(int, input().split()))
count = 0
now = 1

for i in range(len(A)):
    if A[i] == now:
        now += 1
    else:
        count += 1

print(count if now != 1 else -1)