s = input()
n = int(input())

def f(s):
    prev = ''
    ct = 0
    for i in s:
        if i == prev:
            ct += 1
            prev = ''
        else:
            prev = i
    return ct
        

if len(set(s)) == 1:
    print(len(s) *n//2)
elif s[0]!=s[-1]:
    print(f(s) * n)
else:
    ans = f(s) + (f(s*2) - f(s)) * (n-1)
    print(ans)
    
    
