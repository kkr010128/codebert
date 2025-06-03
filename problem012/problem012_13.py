def maybe_prime(d,s,n):
    for a in (2,3,5,7):
        p = False
        x = pow(a,d,n)
        if x==1 or x==n-1:
            continue
        for i in range(1,s):
            x = x*x%n
            if x==1: return False
            elif x == n-1:
                p = True
                break
        if not p: return False
    return True

def is_prime(n):
    if n in (2,3,5,7): return True
    elif n%2==0: return False
    else:
        d,s = n-1, 0
        while not d%2:
            d,s = d>>1,s+1
        return maybe_prime(d,s,n)
cnt = 0
n = int(input())
for i in range(n):
  n = int(input())
  if is_prime(n): cnt+=1

print(cnt)