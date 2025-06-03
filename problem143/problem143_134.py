k = int(input())
s =str(input())
s_print = ''

if k >= len(s):
    print(s)
    exit()
else:
    for i in range(k):
        s_print += s[i]
    s_print += '...'
print(s_print)