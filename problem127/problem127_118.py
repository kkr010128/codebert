X, Y = map(int, input().split())
ans = "No"
for i in range(101) :
    for j in range(101) :
        if(i + j != X) :
            continue
        if(2*i + 4*j != Y) :
            continue
        ans = "Yes"
        break
print(ans)