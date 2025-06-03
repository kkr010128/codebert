n = int(input())

ss = {}
tt = []
for i in range(n):
    s, t = map(str, input().split())
    ss[s] = i + 1
    tt.append(t)

x = input()

print(sum([int(x) for x in tt[ss[x]:]]))