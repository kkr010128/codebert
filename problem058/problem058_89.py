def solve(n,x):
    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j :
                continue
            for k in range(1,n+1):
                if j == k or i == k:
                    continue
                if i+j+k == x:
                    count += 1
    return count//6

while True:
    n,x = map(int,input().split())
    if n == x == 0:
        break;
    print(solve(n,x))