s = input()
a = [-1] * (len(s) + 1)

if s[0] == "<":
    a[0] = 0
if s[-1] == ">":
    a[-1] = 0
    
for i in range(len(s) - 1):
    if s[i] == ">" and s[i + 1] == "<":
        a[i + 1] = 0 

for i in range(len(a)):
    if a[i] == 0:
        l = i - 1
        while 0 <= l - 1:
            if s[l] == ">" and s[l - 1] == ">":
                a[l] = a[l + 1] + 1
            else:
                break
            l -= 1
        r = i + 1
        while r + 1< len(a):
            if s[r - 1] == "<" and s[r] == "<":
                a[r] = a[r - 1] + 1
            else:
                break
            r += 1

for i in range(len(a)):
    if a[i] == -1:
        if i == 0:
            a[i] = a[i + 1] + 1
        elif i == len(a) - 1:
            a[i] = a[i - 1] + 1
        else:
            a[i] = max(a[i - 1], a[i + 1]) + 1
            
ans = sum(a)
print(ans)