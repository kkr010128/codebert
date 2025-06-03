s = input()
l1 = len(s)
res = 0
for i in range(l1//2):
    if s[i]!=s[-i-1]:res +=1
print(res)