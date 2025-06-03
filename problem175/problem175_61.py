n = int(input())
s = input()
ans = s.count('R')*s.count('G')*s.count('B')
for i in range(n-2):
    for j in range(i, n-1):
        if s[i] != s[j]:
            if 2*j-i <= n-1 and s[i]!=s[j] and s[i]!=s[2*j-i] and s[j]!=s[2*j-i]:
                ans -= 1
print(ans)