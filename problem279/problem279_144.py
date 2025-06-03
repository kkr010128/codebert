n = int(input())
s = input()
if n % 2 == 1:
    print('No')
else:
    sa = s[:n//2]
    sb = s[n//2:]
    if sa == sb:
        print('Yes')
    else:
        print('No')