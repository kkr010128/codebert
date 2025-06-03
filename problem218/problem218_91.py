from collections import Counter

n = int(input())
s = Counter([str(input()) for _ in range(n)])
l = []
c = 1

for stri, count in s.items():
    if count == c:
        c = count
        l.append(stri)
    elif count > c:
        c = count
        l.clear()
        l.append(stri)


sort_l = sorted(l)

for i in sort_l:
    print(i)
