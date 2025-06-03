s = list(input())

k = int(input())

n = len(s)

if(len(set(s)) == 1):
    print(n*k//2)
else:
    t = 0
    c = 1
    for i in range(n-1):
        if(s[i] == s[i+1]):
            c += 1
        else:
            t += c // 2
            c = 1
    t += c // 2
    if(s[0] != s[-1]):
        print(t*k)
    else:
        a = 0
        b = 0
        for i in range(n):
            if(s[i] == s[0]):a+=1
            else:break
        for i in range(n)[::-1]:
            if(s[i] == s[-1]):b+=1
            else:break
        print(t*k - (a//2 + b//2 - (a+b)//2) * (k-1))