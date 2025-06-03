D = int(input())
c = list(map(int,input().rstrip().split(" ")))
s = []
t = []
kankaku = [0 for i in range(27)]
last = [0 for i in range(27)]
man = 0
for i in range(D):
    s.append(list(map(int,input().rstrip().split(" "))))
for i in range(D):
    t.append(int(input())-1)
for i in range(D):
    man += s[i][t[i]]
    last[t[i]] = i + 1
    for i2 in range(26):
        man -= (i + 1 - last[i2]) * c[i2]
    print(man)