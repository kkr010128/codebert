n,m = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse = True)
s = sum(A)
cnt = 0
for a in A:
    if a*4*m >= s:
        cnt += 1
    if cnt >= m:
        print('Yes')
        break
else:
    print('No')