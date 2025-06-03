n = int(input())
s = input()
res = 'Yes' if s[0:n//2] == s[n//2:] else 'No'
print(res)