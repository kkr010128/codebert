s = input()
n = len(s)
Ans = [0] * (n + 1)

top = set()
bottom = set()
if s[0] == ">":
    top.add(0)
else:
    bottom.add(0)

for i in range(len(s)-1):
    left = s[i]
    right = s[i+1]
    if left == "<" and right == ">":
        top.add(i+1)
    elif left == ">" and right == "<":
        bottom.add(i+1)

if s[n-1] == ">":
    bottom.add(n)
else:
    top.add(n)

for b in list(bottom):
    counter = 0
    for i in range(b, n+1):
        if i in top:
            break
        else:
            Ans[i] = counter
            counter += 1

    counter = 0
    for i in range(b-1, -1, -1):
        if i in top:
            break
        else:
            Ans[i] = counter + 1
            counter += 1
#print(Ans)

for t in list(top):
    if t == 0:
        Ans[0] = Ans[1] + 1
    if t == n:
        Ans[n] = Ans[n-1] + 1
    else:
        Ans[t] = max(Ans[t-1] + 1, Ans[t+1] + 1)

#print(top)
#print(bottom)
print(sum(Ans))