n = int(input())
s = input()
ans = 0
ans = s.count('R')*s.count('G')*s.count('B')
for i in range(0,n-2):
    for j in range(1,n-1):
        k = -i + 2*j
        if j < k <= n-1:
            if s[i] == s[j]:
                continue
            if s[i] == s[k]:
                continue
            if s[j] == s[k]:
                continue
        else:
            continue
        ans -= 1 
print(ans)