a, b = map(int, input().split())
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
c = factorization(a)
d = factorization(b)
cnt = 1
for i,j in c:
  for k,l in d:
    if i == k:
      cnt += 1
print(cnt)