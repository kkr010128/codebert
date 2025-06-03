s,t = [x for x in input().split()]
a,b = [int(x) for x in input().split()]
ss = input()

if ss == s:
    print(a-1,b)
else:
    print(a,b-1)
