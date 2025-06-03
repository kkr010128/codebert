N = int(input())

def divisor(n):
    if n==1:return []
    ret = [n]
    for i in range(2,n+1):
        if i*i==n:
            ret.append(i)
        elif i*i > n:
            break
        elif n%i==0:
            ret.append(i)
            ret.append(n//i)
    ret.sort()
    return ret

ans = len(divisor(N-1))

for k in divisor(N):
    M = N
    while M%k==0:
        M//=k
    if M%k==1:
        ans += 1
print(ans)