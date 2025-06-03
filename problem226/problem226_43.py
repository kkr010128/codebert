(H,N) = map(int,input().split())
a = [int(x) for x in input().split()]
sum = 0
for i in range(N):
    sum += a[i]
if sum >= H:
    print("Yes")
else:
    print("No")