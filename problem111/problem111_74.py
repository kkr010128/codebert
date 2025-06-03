n = int(input())
A = [0] + sorted(list(map(int, input().split())), reverse=True)
res = A[1] + sum(A[2:(n//2)+1]) * 2
if n % 2 == 0:
    print(res)
else:
    res += A[n//2 + 1]
    print(res)