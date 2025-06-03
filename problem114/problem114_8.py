def complain(comp,c,k,last_hold,i):
    # print(k)
    if(k > 26):
        # print("___")
        return comp
    comp += c[k-1]*((i+1) - last_hold[k-1]) 
    k += 1
    # print(comp,"comp")
    return complain(comp,c,k,last_hold,i)

D = int(input())
c = list(map(int,input().split()))
s = ["_"]*(D)
# print(c)
for i in range(D):
    s[i] = list(map(int,input().split()))
last_hold = [0]*26
score = [0]*(D+1)

for i in range(D):
    score[i+1] += score[i]
    t = int(input())
    last_hold[t-1] = i+1
    comp = 0
    k = 1
    score[i+1] += s[i][t-1]    
    # print(s[i][t-1],"s")
    comp = complain(comp,c,k,last_hold,i)    
    score[i+1] -= comp
    # print(comp,"comp")
    # print(score[i+1],"score")

for i in range(D):
    print(score[i+1])

# Σ(Ci * (d - last(d,i)))
# (1~26)

# 18398
# 35037
# 51140
# 65837
# 79325