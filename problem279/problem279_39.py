n = int(input())
s = input()
a = s[:n//2]
b = s[n//2:]
if a == b:
    print('Yes')
else:
    print('No')