n = int(input())
s = input()
for i in s:
    i = ord(i) + n
    if (i > 90):
        d = i - 90
        print(chr(64+d),end = '')
    else:
        print(chr(i),end = '')