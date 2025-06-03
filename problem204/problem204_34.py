S = input()
Q = int(input())

rev = False
l, r = "", ""

for _ in range(Q):
    query = input()
    if query[0] == "1":
        rev = not rev
    else:
        T, F, C = query.split()
        if F == "1":
            if rev:
                r += C
            else:
                l = C + l
        else:
            if rev:
                l = C + l
            else:
                r += C

res = l + S + r
if rev:
    res = res[::-1]

print(res)