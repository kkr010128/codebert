memo = []
counter = 0
while(True):
    m,f,r = list(map(int,input().split()))
    if m is -1 and r is -1 and f is -1:
        break
    elif m is -1 or f is -1 or m + f < 30:
        memo.append("F")
    elif 30 <= m + f < 50 :
        if r >= 50:
            memo.append("C")
        else:
            memo.append("D")
    elif 50 <= m + f < 65:
        memo.append("C")
    elif 65 <= m + f < 80:
        memo.append("B")
    elif 80 <= m + f:
        memo.append("A")
    counter += 1
for i in range(counter):
    print(memo[i])