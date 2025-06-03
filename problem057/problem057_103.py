num = []
while True:
    m,f,r = map(int, raw_input().split())

    ans = m + f
    if m == f == r == -1:
        break
    if (m == -1) or (f == -1):
        num.append("F")
    elif ans >= 80:
        num.append("A")
    elif (65 <= ans) and (ans < 80):
        num.append("B")
    elif (50 <= ans) and (ans < 65):
        num.append("C")
    elif (30 <= ans) and (ans < 50):
        if r >= 50:
            num.append("C")
        else:
            num.append("D")
    else:
        num.append("F")

for i in range(len(num)):
    print num[i]