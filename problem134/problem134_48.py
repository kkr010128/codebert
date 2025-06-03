n = int(input())
A = list(map(int,input().split()))
if 0 in A:
    print(0)
    exit()
A.sort(reverse=True)
cnt = A[0]
for a in A[1:]:
    cnt *= a
    if cnt > 10 ** 18:
        cnt = -1
        break
print(cnt)