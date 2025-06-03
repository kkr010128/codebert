s1 = []
s2 = []
a = 0
s = input()
for i in range(len(s)):
    if s[i] == "\\":
        s1.append(i)
    elif s[i] == "/" and len(s1)>0:
        j = s1.pop()#position of nearest \
        a += i-j
        a_splt = i-j
        while(len(s2) > 0 and s2[-1][0] > j):
            a_splt += s2.pop()[1]
        s2.append([j, a_splt])

print(a)
ans = ""
ans += str(len(s2))
for area in s2:
    ans += " " + str(area[1])
print(ans)
