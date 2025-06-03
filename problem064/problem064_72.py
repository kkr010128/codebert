s = input()
p = input()
bl = True
if p in s:
    print("Yes")
    bl = False
if bl:
    for i in range(1,len(s)+1):
        if p[0:i] == s[-i:]:
            if p[i:] == s[0:len(p)-i]:
                print("Yes")
                bl = False
                break
if bl:
    print("No")