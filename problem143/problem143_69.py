k = int(input())

s = input()

s = s if len(s) <= k else s[0:k] + '...'

print(s)