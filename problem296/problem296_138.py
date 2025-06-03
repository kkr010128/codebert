s = input()
k = int(input())

if len(set(s)) == 1:
    print((len(s)*k)//2)
else:
    t = [1]
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            t[-1] += 1
        else:
            t.append(1)
    a = 0
    for i in t:
        a += (i//2)*k
    if s[0] == s[-1]:
        if t[0] % 2 == t[-1] % 2 == 1:
            a += k-1
    print(a)