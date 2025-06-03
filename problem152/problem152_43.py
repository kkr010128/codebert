def count(i, s):
    left = right = 0
    for e in s:
        if e == "(":
            left += 1
        else:
            if left == 0:
                right += 1
            else:
                left -= 1

    return left-right, left, right, i


n = int(input())
S = [input() for i in range(n)]
s1 = []
s2 = []
for i, e in enumerate(S):
    c = count(i, e)
    # print(i, c)
    if c[0] >= 0:
        s1.append((c[2], c[3]))
    else:
        s2.append((-c[1], c[3]))

s1.sort()
s2.sort()
# print(s1, s2)
s = []
for e in s1:
    s.append(S[e[1]])
for e in s2:
    s.append(S[e[1]])
# print(s)

_, left, right, _ = count(0, "".join(s))
if left == right == 0:
    print("Yes")
else:
    print("No")

