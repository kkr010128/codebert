s = input()
q = int(input())
for i in range(q):
    inp = input().split()
    order = inp[0]
    params = inp[1:]
    if order == "print":
        a,b = map(int,params)
        print(s[a:b+1])
    elif order == "reverse":
        a,b = map(int,params)
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    elif order == "replace":
        a,b,p = params
        a = int(a)
        b = int(b)
        s = s[:a] + p  + s[b+1:]