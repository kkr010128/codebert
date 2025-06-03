n = int(input())
d = {}
t = [0]*n
for i in range(n):
    S,T = input().split()
    d[S] = i
    t[i] = int(T)
x = input()
idx = d[x]

print(sum(t[idx+1:]))
