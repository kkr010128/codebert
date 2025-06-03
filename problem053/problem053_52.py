n = input()
a = map(int, raw_input().split())
if len(a) == n:
    a.reverse()
    print ' '.join(map(str, a))