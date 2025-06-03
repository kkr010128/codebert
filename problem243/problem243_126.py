n = int(input())
s = []
t = []
for i in range(n):
    si, ti = input().split()
    s.append(si)
    t.append(int(ti))
x = input()

insleep = s.index(x)
ans = sum(t[insleep+1:])
print(ans)