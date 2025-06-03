n, m = map(int, input().split())
s = []
c = []

for _ in range(m):
    S, C = map(int, input().split())
    s.append(S)
    c.append(C)

for i in range(m):
    if s[i] == 1 and c[i] == 0 and n != 1:
        print(-1)
        exit()

for i in range(m):
    for j in range(m-1):
        if s[i] == s[-j-1] and c[i] != c[-j-1]:
            print(-1)
            exit()

if n == 3:
    one_hundred = False
    ten = False
    one = False
    for i in range(m):
        if s[i] == 1:
            one_hundred = c[i]
        elif s[i] == 2:
            ten = c[i]
        else:
            one = c[i]
    if one_hundred == False:
        one_hundred = 1
    if ten == False:
        ten = 0
    if one == False:
        one = 0
    print(one_hundred*100 + ten*10 + one)
    exit()
elif n == 2:
    ten = False
    one = False
    for i in range(m):
        if s[i] == 1:
            ten = c[i]
        else:
            one = c[i] 
    if ten == False:
        ten = 1
    if one == False:
        one = 0
    print(ten*10 + one)
    exit()
else:
    one = False
    for i in range(m):
        if s[i] == 1:
            one = c[i]
    if one == False:
        one = 0
    print(one)
    exit()

print(-1)