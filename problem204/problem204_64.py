s = input()
q = int(input())

f1 = 1
f2 = 2

st = ""
se = ""

for _ in range(q):
    q = input().split()
    if int(q[0]) == 1:
        f1,f2 = f2,f1
    elif int(q[0]) == 2:
            if int(q[1]) == f1:
                st = q[2] + st
            elif int(q[1]) == f2:
                se += q[2]

ans = st + s + se
if f1 == 1:
    print(ans)
else:
    ans = list(ans)
    ans.reverse()
    ans = "".join(ans)
    print(ans)