n = int(input())
a = []
b = []
for i in range(n):
    c,d = map(str, input().split())
    a.append(c)
    b.append(int(d))
s = input()
t = a.index(s)
print(sum(b[t+1:]))