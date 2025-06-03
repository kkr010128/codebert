s = input()
n = int(input())
for _ in range(n):
    O = list(map(str, input().split()))
    i = int(O[1])
    j = int(O[2])
    if O[0] == 'print':
        print(s[i:j + 1])
    elif O[0] == 'reverse':
        ss = s[i:j + 1]
        s = s[:i] + ss[::-1] + s[j + 1:]
    else:
        p = O[3]
        s = s[:i] + p + s[j + 1:]

