n, q = map(int, input().split())

s = list()
process = 0
t = list()
for i in range(n):
    name, time = map(str, input().split())
    s.append([name, int(time)])

flag = True
while s:
    diff = s[0][1] - q
    if diff <= 0:
        process += s[0][1]
        t.append([s[0][0], process])
        s.pop(0)
    else:
        process += q
        s.append([s[0][0], diff])
        s.pop(0)
for i in t:
    print(i[0], i[1])