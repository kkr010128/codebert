s = input()
n = int(input())
for _ in range(n):
    li = input().split()
    op = li[0]
    a, b = map(int, li[1:3])
    if op == "replace":
        p = li[3]
        s = s[:a] + p + s[b+1:]
    elif op == "reverse":
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    elif op == "print":
        print(s[a:b+1])
