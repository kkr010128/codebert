n = int(input())
s = input()

if len(s) % 2 == 1:
    print('No')

else:
    mid = len(s)//2
    if s[:mid] == s[mid:]:
        print('Yes')
    else:
        print('No')