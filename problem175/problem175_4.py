import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
s = list(input())

c  = Counter(s)  

num = c['R']*c['G']*c['B']

for j in range(n):
    for d in range(1,min(j,n-j-1)+1):
        i = j-d
        k = j+d
        if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
            num -= 1
print(num)