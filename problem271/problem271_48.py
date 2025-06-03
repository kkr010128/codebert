n = int(input())
s = list(input())
a = []
for i in s:
    num = ord(i)+n
    if num > 90:
        num -= 26
    a.append(chr(num))
print(''.join(a))