input()
s = set(map(int,input().split()))
n = int(input())
t = tuple(map(int,input().split()))
c = 0
for i in range(n):
    if t[i] in s:
        c += 1
print(c)