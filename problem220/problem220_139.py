s,t = input().split()
a,b = (int(x) for x in input().split())
u = input()



if u == s:
    print(a - 1,b)
else:
    print(a,b - 1)

