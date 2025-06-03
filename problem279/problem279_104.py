n=int(input())
s = input()
ans = 0

if n%2 != 0:
    print('No')
if n%2 == 0:
    for i in range(n//2):
        if s[i] == s[i+n//2]:
            ans += 1
    if ans == n//2:
        print('Yes')
    if ans != n//2:
        print('No')