n = int(input())
s = []
t = []
ans = 0
for i in range(n):
    s1,t1 = input().split()
    s.append(str(s1))
    t.append(int(t1))
x = str(input())
for j in range(n):
    if s[j] == x:
        print(sum(t[j+1:n+1]))