k = int(input())
s = input()
sen = ''

if len(s) <= k:
    print(s)
else:
    for i in range(k):
        sen = sen + s[i]
    print(sen+'...')
    
