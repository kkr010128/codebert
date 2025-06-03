n = int(input())
data = {}
for i in range(n):
    b, f, r, v = map(int, input().split())
    if (b,f,r) in data:
        data[(b,f,r)] = data[(b,f,r)] + v
    else:
        data[(b,f,r)] = v
for b in range(1,5):
    for f in range(1,4):
        for r in range(1,11):
            if (b,f,r) in data:
               print(" "+str(data[(b,f,r)]),end="")
            else:
                print(" 0",end="")
        print("")
    if b < 4:
        print("#"*20)