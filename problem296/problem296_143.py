s = str(input())
k = int(input())
 
n = len(s)
l = [0] * n

for i in range(n-1):
    if s[i] == s[i+1] and l[i] == 0:
        l[i+1] = 1

if s.count(s[0]) == n:
    print(n*k//2)
elif s[0] != s[-1]:
    print(sum(l) * k)
else:
    a = 0
    b = 0
    ac = True
    bc = True
    for i in range(n-1):
        if s[i] == s[0] and ac == True:
            a += 1
        elif s[i] != s[0]:
            ac = False
        if s[n-1-i] == s[n-1] and bc == True:
            b += 1
        else: bc = False  
    sub = a//2 + b//2 - (a+b)//2
    print(sum(l)*k - sub*(k-1))