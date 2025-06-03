string = input()
num = int(input())
o = 0
for _ in range(num):
    source = input().split(' ')
    if source[0] == 'print':
        print(string[int(source[1]):int(source[2]) + 1])
    elif source[0] == 'replace':
        string = string[:int(source[1])] + source[3] + string[int(source[2]) + 1:]
    else:
        string = string[:int(source[1])] + string[int(source[1]):int(source[2]) + 1 ][::-1] + string[int(source[2]) + 1:]
