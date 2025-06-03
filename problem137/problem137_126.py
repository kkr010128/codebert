n = int(input())

low = [0]*n
high = [0]*n

for i in range(n):
    a, b = [int(x) for x in input().split(" ")]
    low[i] = a
    high[i] = b

low.sort()
high.sort()

if n%2 == 1:
    print(high[n//2]-low[n//2]+1)
else:
    x = (low[(n-1)//2] + low[n//2])/2
    y = (high[(n-1)//2] + high[n//2])/2
    print(int(2*y - 2*x + 1))
