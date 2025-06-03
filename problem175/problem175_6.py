n = int(input())
s = str(input())
r = 0
g = 0
b = 0
for i in range(n):
    if s[i] == "R":
        r += 1
    elif s[i] == "G":
        g += 1
    else:
        b += 1
p = r*g*b
for i in range(n-2):
    for j in range(int(n/2)+1):
        if i + 2*j >n-1:
            break
        if s[i] != s[i+j] and s[i] != s[i+2*j] and s[i+2*j] != s[i+j]:
            p -= 1
print(p)