n = int(input())
cnt = 0
for i in range(1, n//2+1):
    if i != n - i and n - i > 0:
        cnt += 1
print(cnt)
