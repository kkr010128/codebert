def composite(d,n,s):
    for a in (2,3,5,7):
        probably_prime = False
        if pow(a,d,n) == 1:
            continue
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                probably_prime = True
                break
        return not probably_prime
    return False

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        d,s = n-1, 0
        while not d%2:
            d, s = d>>1, s+1
        return not composite(d,n,s)

r = []
n = int(input())
for i in range(n):
  n = int(input())
  if is_prime(n):
      if n not in r:
          r.append(n)

print(len(r))