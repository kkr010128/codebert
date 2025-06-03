s = input()
k = int(input())

tmp = 1
count = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        tmp += 1
    else:
        count += tmp // 2
        tmp = 1
count += tmp//2

if len(set(s))==1:
    print(len(s)*k//2)
else:
    if s[0] != s[-1]:
        print(count*k)
    else:
        h = 0
        for i in s:
            if i != s[0]:
                break
            else:
                h += 1
        t = 0
        for i in s[::-1]:
            if i != s[-1]:
                break
            else:
                t += 1
        print(count*k-(h//2+t//2-(h+t)//2)*(k-1))
