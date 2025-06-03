ini = lambda : int(input())
inm = lambda : map(int,input().split())
inl = lambda : list(map(int,input().split()))
gcd = lambda x,y : gcd(y,x%y) if x%y else y
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
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

#maincode-------------------------------------------------
n = ini()
s = input()
r = s.count('R')
g = s.count('G')
b = s.count('B')
ans = r*g*b

for j in range(n):
    for i in range(j):
        k = 2*j-i
        if k < n:
            if (s[i] == s[j]):
                continue
            if (s[i] == s[k]):
                continue
            if (s[j] == s[k]):
                continue
            ans -= 1
print(ans)