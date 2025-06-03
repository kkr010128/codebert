m, n = map(int, input().split())
l = list(map(int, input().split()))

for i in range(m-n):
    if l[i] < l[i+n]:
        print('Yes')
    else:
        print('No')
