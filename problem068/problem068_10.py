s = list(input())
q = int(input())

rvs = []
i = 0
j = 0
p = []
order = []
for i in range(q):
    
    order.append(input().split())
    
    if order[i][0] == "replace":
        p = []
        p = list(order[i][3])

        for j in range(int(order[i][1]), int(order[i][2]) + 1):
            s[j] = p[j - int(order[i][1])]

    elif order[i][0] == "reverse":
        ss = "".join(s[int(order[i][1]):int(order[i][2]) + 1])
        rvs = list(ss)
        rvs.reverse()
        for j in range(int(order[i][1]), int(order[i][2]) + 1):
            s[j] = rvs[j - int(order[i][1])]
        
        # temp = s[int(order[i][1])]
        # s[int(order[i][1])] = s[int(order[i][2])]
        # s[int(order[i][2])] = temp

    elif order[i][0] == "print":
        ss = "".join(s)
        print("%s" % ss[int(order[i][1]):int(order[i][2]) + 1])


