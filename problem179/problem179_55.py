n,m = map(int, input().split())
A = list(map(int, input().split()))
rank = sum(A) / (4*m)
cnt =0

for a in A:
    cnt += rank <= a

if cnt >= m:
    print('Yes')
else:
    print('No')