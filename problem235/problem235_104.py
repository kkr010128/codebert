import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
mod = 10**9+7
num = tuple(num)

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
  j = factorization(i)
  for x,y in j:
    if not x in lcd.keys():
      lcd[x] = y
    else:
      lcd[x] = max(lcd[x],y)

lc = 1
for i,j in lcd.items():
  lc *= pow(i,j,mod)
  
ans =0
for i in range(n):
  ans += lc*pow(num[i], mod-2, mod)
  ans %= mod
print(ans)