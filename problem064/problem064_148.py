s = list(input())
p = list(input())
for x in range(len(p)) :
    s.append(s[x])

i = 0
j = 0
while True :
    if p[j] == s[i] :
        j += 1
        if j == len(p) :
            print("Yes")
            break
        i += 1
        if i == len(s) :
            print("No")
            break
    else :
        i += (1 - j)
        if i == len(s) :
            print("No")
            break
        j = 0

