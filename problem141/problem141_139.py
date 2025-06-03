n = int(input())
As = list(map(int, input().split()))

internal_max = [1]*(n+1)
internal_max[0] = 1-As[0]

for i in range(1,n+1):
    internal_max[i] = 2*internal_max[i-1]-As[i]

depth_sum = [0]*(n+1)
depth_sum[n] = As[n]
judge = False

for i in range(n-1, -1, -1):
    if depth_sum[i+1] > internal_max[i]*2:
        judge = True
        break
    else:
        depth_sum[i] = As[i] + min(internal_max[i], depth_sum[i+1])

if n == 0:
    if As[0] > 1:
        judge = True

if judge:
    print(-1)
else:
    print(sum(depth_sum))
