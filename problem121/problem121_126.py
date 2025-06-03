n = int(input())

str = ""

while 1:
    n, mod = divmod(n, 26)
    if mod == 0:
        str = 'z' + str
        n -=1
    else:
        str = chr(96+mod) + str

    if n == 0:
        break

print(str)