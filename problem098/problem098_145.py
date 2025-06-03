def abc174d():
    n = int(input())
    s = input()
    cnt = s.count('R')
    if cnt == len(s):
        print(0)
        return
    start = 0
    while s[start] == 'R':
        start += 1
        cnt -= 1
    ans = cnt
    for i in range(start, start+cnt):
        if s[i] == 'R':
            ans -= 1
    print(ans)
abc174d()