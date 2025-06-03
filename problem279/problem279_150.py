n = int(input())
s = input()

if n % 2 == 1:
    print('No')
    exit()

mid= int(len(s)/2)
if s[:mid] == s[mid:]:
    print('Yes')
else:
    print('No')
