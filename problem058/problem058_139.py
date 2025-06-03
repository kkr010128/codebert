def solve(n,x):
    count = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            k = x - i - j
            if j < k and k <= n:
                count += 1
    return count

while True:
    n,x = map(int,input().split())
    if n == x == 0:
        break;
    print(solve(n,x))