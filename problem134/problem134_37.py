N = int(input())
alist = list(map(int, input().split()))
k = 1
if 0 in alist:
    print(0)
else:
    for i in range(0,N):
        k = k*alist[i]
        if k > 1000000000000000000:
            k= -1
            break
    print(k)