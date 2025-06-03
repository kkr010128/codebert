n = int(input())
s = input()
t = ""
for i in range(n // 2):
    t += s[i]
    
if s == (t + t):
    print('Yes')
else:
    print('No')