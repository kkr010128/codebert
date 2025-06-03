s = list(input())
q = int(input())
l1 = []
l2 = []
rev = False
for i in range(q):
    inp = input()
    if inp[0] == "1":
        if rev:
            rev = False
        else:
            rev = True
    elif inp[2] == "1":
        a = inp[4]
        if rev:
            l2.append(a)
        else:
            l1.append(a)
    else:
        a = inp[4]
        if rev:
            l1.append(a)
        else:
            l2.append(a)
l1.reverse()
ans = l1 + s + l2
if rev:
    ans.reverse()
print("".join(ans))