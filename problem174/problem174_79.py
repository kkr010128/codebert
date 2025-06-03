N = int(input())
kotae = []
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            s = i
            t = j
            u = k
            x = 1
            while x != 0:
                v = t%s
                if v != 0:
                    t = s
                    s = v
                else:
                    t = s
                    x = u%t
                    if x != 0:
                        u = t
                        t = x
                    else:
                        kotae.append(t)
print(sum(kotae))