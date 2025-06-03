n = int(input())
s = list(input())
cnt = 0
if n % 2 != 0 :
    print('No')
    exit()
for i in range(n//2):
    if s[i] != s[i + n // 2]:
        print('No')
        exit()

print('Yes')