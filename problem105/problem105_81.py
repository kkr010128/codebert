N = int(input())
A = map(int, input().split())
cnt = 0
for i, a in enumerate(A):
    if ((i + 1) * a) % 2:
        cnt += 1
print(cnt)
