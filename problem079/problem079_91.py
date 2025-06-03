s = int(input())
n = [1,0,0]
if s < 3:
    print(n[s])
else:
    for i in range(s-2):
        n.append(n[-1]+n[-3])
    print((n[-1])%1000000007)