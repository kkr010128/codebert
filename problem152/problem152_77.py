n = int(input())
s = [input() for _ in range(n)]

l = 0
r = 0
m = []


def fin():
    print("No")
    exit()


for word in s:
    stack = []
    for e in word:
        if stack and stack[-1] == "(" and e == ")":
            stack.pop()
        else:
            stack.append(e)

    if stack:
        if stack[0] == ")" and stack[-1] == "(":
            m.append(stack)
        elif stack[0] == ")":
            r += len(stack)
        else:
            l += len(stack)

ml = []
mm = 0
mr = []

for word in m:
    ll = word.index("(")
    rr = len(word) - ll
    if ll > rr:
        mr.append([ll, rr])
    elif ll < rr:
        ml.append([ll, rr])
    else:
        mm = max(mm, ll)

ml.sort()
for ll, rr in ml:
    l -= ll

    if l < 0:
        fin()

    l += rr

mr.sort(key=lambda x: x[1])
for ll, rr in mr:
    r -= rr

    if r < 0:
        fin()

    r += ll

if mm <= l or mm <= r:
    if l == r:
        print("Yes")
        exit()

fin()
