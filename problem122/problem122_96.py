n = int(input())
li_a = list(map(int, input().split()))
dic_a = {}

for a in li_a:
    dic_a[a] = dic_a.get(a, 0) + 1

q = int(input())
li_bc = list()

for i in range(q):
    li_bc.append(tuple(map(int, input().split())))


answer = sum(li_a)
for l in li_bc:
    b = l[0]
    c = l[1]

    diff = (c - b) * dic_a.get(b, 0)
    if b in dic_a.keys():
        dic_a[c] = dic_a.get(c, 0) + dic_a.get(b, 0)
        dic_a[b] = 0
        answer += diff
    else:
        pass
    print(answer)
