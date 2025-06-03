s = input()
a = list(s)

for i in range(len(s)):
    a[i] = 'x'
    
ans = "".join(a)
    
print(ans)