s = list(input())
t = list(input())

ans = 1000
sub = 0
flag = False
for i in range(len(s)):
    if s[i] != t[sub]:
        sub = 0
        continue
    else:
        if sub == len(t) - 1:
            print(0)
            flag = True
            break
        sub += 1

if not flag:
    for i in range(len(s) - len(t) + 1):
        sub = 0
        an = 0
        for j in range(len(t)):
            if s[i + j] != t[sub]:
                an += 1
            sub += 1 
        ans = min(an, ans)

    print(ans)