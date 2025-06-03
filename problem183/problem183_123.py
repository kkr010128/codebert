N = int(input())
if N ==2:
  print(1)
  exit()

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
 
    if temp!=1: #素数の場合はここ
        arr.append([temp, 1])
 
    if arr==[]: #1の場合はここ
        arr.append([n, 1])
 
    return arr

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
A = make_divisors(N)
ans = 0 #自分自身の一個を足しておく
SET = set([N])
#print(A)
for i in range(1,len(A)):
  M = N*1
  while M%A[i]==0:
    M = M//A[i]
  if M%A[i] == 1:
    ans += 1
    SET.add(A[i])
#ans = len(SET)
#print(SET)
#print(ans)
N -= 1
B = factorization(N)
yakusu = 1
#print(B)
for i in range(len(B)):
  yakusu *= (B[i][1]+1)
#print(yakusu)
ans += yakusu-1
print(ans)
