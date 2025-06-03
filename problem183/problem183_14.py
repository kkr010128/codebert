N = int(input())

if N == 2:
  print(1)
  exit()

ans = 0

def factorization(n):
  lis = []
  if n % 2 == 0:
    c = 0
    while n%2 == 0:
      n //= 2
      c += 1
    lis.append([2, c])
  k = 3
  while k*k <= n:
    if n%k == 0:
      c = 0 
      while n%k == 0:
        n //= k
        c += 1
      lis.append([k, c])
    else:
      k += 2
  if n > 1:
    lis.append([n, 1])
  return lis

list1 = factorization(N-1)
ans1 = 1
for k in range(len(list1)):
  ans1 *= list1[k][1]+1
ans += ans1-1

def operation(K):
  n = N
  while n%K == 0:
    n //= K
  if n%K == 1:
    return True
  else:
    return False

list2 = factorization(N)
factorlist = [1]
for l in range(len(list2)):
  list3 = []
  for j in range(list2[l][1]):
    for k in range(len(factorlist)):
      list3.append(factorlist[k]*list2[l][0]**(j+1))
  factorlist += list3
factorlist = factorlist[1:-1]
ans += 1
for item in factorlist:
  if operation(item):
    ans +=1
print(ans)