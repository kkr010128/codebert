N = int(input())
a = list(map(int, input().split()))
left = []
for i in range(N):
    if left:
        if a[i] == left[-1] + 1:
            left.append(a[i])
    else:
        if a[i] == 1:
            left.append(a[i])
if left:
    print(N - len(left))
else:
    print(-1)