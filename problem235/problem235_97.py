import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
mod = 10**9+7

# 高速素因数分解(√n)
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
    if arr==[]:
        arr.append([n, 1])
    return arr

lcd = dict()
for i in num:
  j = dict(factorization(i))
  for x,y in j.items():
    if not x in lcd.keys():
      lcd[x] = y
    else:
      lcd[x] = max(lcd[x],y)

lc = 1
for i,j in lcd.items():
  lc *= pow(i,j,mod)
  
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

ans =0
for i in range(n):
  ans += lc*modinv(num[i],mod)
  ans %= mod
print(ans)