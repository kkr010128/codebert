def inN():
    return int(input())
def inL():
    return list(map(int,input().split()))
def inNL(n):
    return [list(map(int,input().split())) for i in range(n)]


n = inN()
s = input()


r = s.count('R')
b = s.count('B')
g = s.count('G')
cnt = 0

for i in range(n):
    for j in range(i+1,n):
        k = 2*j - i
        if k < n:
            if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                cnt += 1
print(r*g*b - cnt)