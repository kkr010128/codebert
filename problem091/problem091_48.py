def check(a,b,c):
    if a == b:
        return False
    if b == c:
        return False
    if c == a:
        return False
    m = max(a,b,c)
    if m >= (a+b+c)-m:
        return False
    return True

N = int(input())
L = list(map(int,input().split()))
ans = 0
if N >= 3:
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if check(L[i],L[j],L[k]):
                    ans += 1
print(ans)