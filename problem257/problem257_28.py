N = int(input())

A = list(map(int,input().split()))


tmp = 1
counter = 0
for a in A:
    if a==tmp:
        counter += 1
        tmp += 1

if counter==0:
    print(-1)
else:
    print(N-counter)

