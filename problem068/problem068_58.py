def my_print(s, a, b):
    print(s[a:b+1])

def my_reverse(s, a, b):
    return s[:a] + s[a:b+1][::-1] + s[b+1:]

def my_replace(s, a, b, p):
    return s[:a] + p + s[b+1:]

if __name__ == '__main__':
    s = input()
    q = int(input())
    for i in range(q):
        code = input().split()
        op, a, b = code[0], int(code[1]), int(code[2])
        if op == 'print':
            my_print(s, a, b)
        elif op == 'reverse':
            s = my_reverse(s, a, b)
        elif op == 'replace':
            s = my_replace(s, a, b, code[3])