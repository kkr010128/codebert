code = input()
n = int(input())

for i in range(n):
    lst = list(input().split())
    a = int(lst[1])
    b = int(lst[2])

    if lst[0] == 'replace':
        t1 = code[0:a]
        t2 = code[a:b+1]
        t3 = code[b+1:len(code)]
        code = t1 + lst[3] + t3

    elif lst[0] == 'reverse':
        s = code[a:b+1]
        ss = ''.join(list(reversed(s)))
        t1 = code[0:a]
        t2 = code[a:b+1]
        t3 = code[b+1:len(code)]
        code = t1 + ss + t3

    elif lst[0] == 'print':
        print(code[a:b+1])
