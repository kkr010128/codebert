N = int(input())
s = {}
t = []
for i in range(N):
    st = input().split()
    s[st[0]] = i
    t.append(int(st[1]))
X = input()
print(sum(t[s[X]+1:]))