ans = ''
while True:
    s = input()
    if s == '-':
        break
    n = int(input())
    L = []
    i = 0
    while i < n:
        j = int(input())
        s = s[j:] + s[:j]
        i += 1
    ans += s + '\n'
if ans != '':
    print(ans[:-1])
