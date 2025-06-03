n = int(input())
s = input()

if n%2 != 0:
    ans = 'No'
else:
    ans = 'Yes'
    for i in range(n//2):
        if s[i] != s[i+n//2]:
            ans = 'No'
print(ans) 