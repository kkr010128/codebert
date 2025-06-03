import sys
s = input()
k = int(input())
n = len(s)
if n==1:
    print(k//2)
    sys.exit()
if n==2:
    print(k if s[0]==s[1] else 0)
    sys.exit()
i = 1
change = [0, 0]
same = True
while i<n:
    if s[i-1]==s[i]:
        if i==n-1:
            same = False
        change[0] += 1
        i += 1
    i += 1
if s[0]!=s[-1]:
    same = False
if not same:
    print(change[0]*k)
    sys.exit()
i = 2
change[1] = 1
same = True
while i<n:
    if s[i-1]==s[i]:
        if i==n-1:
            same = False
        change[1] += 1
        i += 1
    i += 1
if same:
    print(change[0]+change[1]*(k-1))
else:
    print(change[0]*((k+1)//2)+change[1]*(k//2))