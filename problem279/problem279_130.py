n = int(input())
s = input()
ans = 'No'

if n%2 == 0:
    mid = int(n/2)
    if s[:mid] == s[mid:]:
        ans = 'Yes'

print(ans)