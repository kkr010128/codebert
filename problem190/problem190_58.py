s = input()
ans = 'Yes'
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        ans = 'No'
        break
        
s_s = s[:(len(s)-1)//2]
for i in range(len(s_s)//2):
    if s_s[i] != s_s[-i-1]:
        ans = 'No'
        break
        
s_e = s[(len(s)+3)//2 - 1:]
for i in range(len(s_e)//2):
    if s_e[i] != s_e[-i-1]:
        ans = 'No'
        break
        
print(ans)