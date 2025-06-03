a, b, c, d = map(int, input().split())
 
if b >= 0 and d >= 0 and a <= 0 and c <= 0:# - + - +
    e = b*d
    f = a*c
    if e > f:
        print(e)
    else:
        print(f)
elif a >= 0 and b >= 0 and c >= 0 and d >= 0: #+ + + +
    print(b*d)
elif a <= 0 and b <= 0 and c <= 0 and d <= 0: #- - - -
    print(a*c)
elif a >= 0 and b >= 0 and c <= 0 and d <= 0: #+ + - -
    print(a*d)
elif a >= 0 and b >= 0 and c <= 0 and d >= 0: # + + - +
    print(b*d)
elif a <= 0 and b <= 0 and c >= 0 and d >= 0: # - - + +
    print(b*c)
elif a <= 0 and b <= 0 and c <= 0 and d >= 0: # - - - +
    print(a*c)
elif a <= 0 and b >= 0 and c >= 0 and d >= 0: # - + + +
    print(b*d)
elif a <= 0 and b >= 0 and c <= 0 and d <= 0: # - + - -
    print(a*c)