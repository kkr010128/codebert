n = int(input())

a = []
b = []
for i in range(n):
    s = input()
    x = 0
    y = 0
    for c in s:
        if c == '(':
            y += 1
        else:
            if y >= 1:
                y -= 1
            else:
                x += 1
    if x < y: a.append([x, abs(x-y)])
    else: b.append([y, abs(x-y)])

def calc(a):
    ret = 0
    for x, y in sorted(a):
        if ret < x: return -1
        ret += y
    return ret
   
res1 = calc(a)
res2 = calc(b)
print("Yes" if res1 >= 0 and res1 == res2 else "No")