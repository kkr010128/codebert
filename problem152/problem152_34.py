import math
import fractions
#import sys
#input = sys.stdin.readline

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def ValueToBits(x,digit):
    res = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        res[i]=now%2
        now = now >> 1
    return res

def BitsToValue(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans+= arr[i] * 2**i
    return ans

def ZipArray(a):
    aa = [[a[i],i]for i in range(n)]

    aa.sort(key = lambda x : x[0])
    for i in range(n):
        aa[i][0]=i+1
    aa.sort(key = lambda x : x[1])
    b=[aa[i][0] for i in range(len(a))]
    return b

def ValueToArray10(x, digit):
    ans = [0 for i in range(digit)]
    now = x
    for i in range(digit):
        ans[digit-i-1] = now%10
        now = now //10
    return ans

def Zeros(a,b):
    if(b<=-1):
        return [0 for i in range(a)]
    else:
        return [[0 for i in range(b)] for i in range(a)]

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
            
'''
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 2
N = 10 ** 6 + 2
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

'''

#a = list(map(int, input().split()))

#################################################
#################################################
#################################################
#################################################



n = int(input())

lr = []

for i in range(n):
    s = input()
    m = len(s)
    #exam left
    count = 0
    left = 0
    for j in range(m):
        if(s[j]=='('):
            count += 1
        else:
            if(count == 0):
                left+=1
            else:
                count -=1
    #exam right
    count = 0
    right = 0
    for j in range(m):
        if(s[m-j-1]==')'):
            count += 1
        else:
            if(count == 0):
                right+=1
            else:
                count -=1

    #print(left,right)
    lr.append([left,right])

existL = 0
existR = 0
sumL = 0
sumR = 0
for i in range(n):
    sumL += lr[i][0]
    sumR += lr[i][1]
    if(lr[i][0]==0 and lr[i][1]!=0):
        existL=1
        #print(lr[i])
    if(lr[i][1]==0 and lr[i][0]!=0):
        existR=1
        #print(lr[i])
lr2 = []
for i in range(n):
    if(lr[i][0]==0): lr2.append(lr[i])
lr3 = []
for i in range(n):
    if(lr[i][0]*lr[i][1]!=0): lr3.append(lr[i])
lr3.sort(key = lambda x : x[0]-x[1])
for i in lr3:
    lr2.append(i)
for i in range(n):
    if(lr[i][1]==0): lr2.append(lr[i])
#print(lr2)

ok = 1
now = 0
for i in range(n):
    now -= lr2[i][0]
    if(now<0):
        ok = 0
        #print('a',lr2[i])
    now += lr2[i][1]
    
if(existL*existR == 1 and sumL == sumR and ok==1):
    print("Yes")
else:
    if(sumL==0 and sumR==0):
        print("Yes")
    else:
        print("No")




































