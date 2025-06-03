#coding:utf-8

ans = []
for i in xrange(20000):
    a, op, b = raw_input().split()
    if op == "?":
        break
    else:
        if op == "+":
            ans.append(int(a) + int(b))
        elif op == "-":
            ans.append(int(a) - int(b))
        elif op == "*":
            ans.append(int(a) * int(b))
        else:
            ans.append(int(a) / int(b))

for n in xrange(len(ans)):
    print(ans[n])