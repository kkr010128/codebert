letters = input()
num = int(input())
for i in range(num):
    order = input().split()
    a = int(order[1])
    b = int(order[2])
    if order[0] == 'print':
        print(letters[a:b+1])
    if order[0] == 'reverse':
        p = letters[a:b+1]
        p = p[::-1]
        letters = letters[:a] + p + letters[b+1:]
    if order[0] == 'replace':
        letters = letters[:a] + order[3] + letters[b+1:]
