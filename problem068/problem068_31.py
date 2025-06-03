if __name__ == '__main__':
    s = input()
    q = int(input())
    for i in range(q):
        code = input().split()
        op, a, b = code[0], int(code[1]), int(code[2])
        if op == 'print':
            print(s[a:b+1])
        elif op == 'reverse':
            s = s[:a] + s[a:b+1][::-1] + s[b+1:]
        elif op == 'replace':
            s = s[:a] + code[3] + s[b+1:]