N = int(input())
A = list(map(int,input().split()))
A.sort()
if N==2:
    print(max(A))
    exit()

ans = A.pop()
n = N-2
while A:
    a = A.pop()
    for _ in range(2):
        n -= 1
        ans += a
        if n==0:
            print(ans)
            exit()