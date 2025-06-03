n = int(input())
s = input()
if n == 1 or n % 2 == 1:
    print('No')
    exit()
mid = n // 2
if s[:mid] == s[mid:]:
    print('Yes')
else:
    print('No')