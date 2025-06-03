n = int(input())
s = list(input())
r = 0
g = 0
b = 0

for c in s:
    if c == "R":
        r += 1
    if c == "G":
        g += 1
    if c == "B":
        b += 1
ans = r*g*b

for i in range(n):
    for j in range(i+1,n):
        k = 2*j - i
        if k > n-1:
            continue
        x = s[i]
        y = s[j]
        z = s[k]
        if x!= y and y != z and z != x:
            ans -= 1

print(ans)