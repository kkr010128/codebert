N, A, B = map(int, input().split())

ans = 0

if abs(B-A) % 2 == 0:
    ans = abs(B-A) // 2

else:
    if B > A:
        ans = min(N-A, B-1,(N-B+1) + (B-A-1)//2, (A-1+1) + (B-A-1)//2)

    if A > B:
        ans = min(N-B, A-1,(N-A+1) + (A-B-1)//2, (B-1+1) + (A-B-1)//2)


print(ans)