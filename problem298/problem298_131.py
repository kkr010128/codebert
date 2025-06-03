n, k = map(int,input().split())
H = sorted(list(map(int, input().split())), reverse=True)
cnt = 0
for i in range(n):
    if H[i] >= k:
        cnt += 1
    elif H[i] < k:
        break
print(cnt)