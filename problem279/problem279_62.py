n = int(input())
s = input()

if n % 2 == 1:
    print('No')
    exit()

flg = True
n2 = n // 2
for i in range(n2):
    if s[i] != s[n2+i]:
        flg = False
        break
print('Yes') if flg else print('No')