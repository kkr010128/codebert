s = input()
flag = 0
sr = s[-1::-1]
if sr == s:
    flag+=1
s1 = s[:(len(s)-1)//2]
s1r = s1[-1::-1]
if s1 == s1r:
    flag += 1
s2 = s[(len(s)+3)//2-1:]
s2r = s2[-1::-1]
if s2 == s2r:
    flag+=1
print('Yes' if flag == 3 else 'No')
