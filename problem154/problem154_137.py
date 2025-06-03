n, k = (int(i) for i in input().split())
used = [0 for i in range(n)]
for i in range(k):
    val = int(input())
    a = [int(j) for j in input().split()]
    for aa in a:
        used[aa - 1] = 1
cnt = 0
for i in used:
    cnt += i == 0
print(cnt)
