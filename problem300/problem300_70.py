def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    return arr

a, b = map(int, input().split())
fa = factorization(a)
fb = factorization(b)

i = 0
j = 0
cnt = 1
while i < len(fa) and j < len(fb):
  if fa[i][0] == fb[j][0]:
    cnt += 1
    i += 1
    j += 1
  elif fa[i][0] < fb[j][0]:
    i += 1
  else:
    j += 1

print(cnt)